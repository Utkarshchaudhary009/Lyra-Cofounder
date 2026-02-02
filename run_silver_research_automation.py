import os
import time
import subprocess
import re
import sys
import json

class Logger(object):
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, "a", encoding='utf-8')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
        self.log.flush()

    def flush(self):
        self.terminal.flush()
        self.log.flush()

def say(text):
    subprocess.run(["say",text])
def main():
    base_path = r"i:\Lyra-Cofounder\@general\research\Silver_Suppression"
    
    # Set up logging to both console and file
    log_file = os.path.join(base_path, "research_automation_log.txt")
    # Only redirect if not already redirected (simple check)
    if not isinstance(sys.stdout, Logger):
        sys.stdout = Logger(log_file)
    
    print(f"\n{'='*60}")
    print(f"Automation Script Started: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Logging to: {log_file}")
    print(f"{'='*60}\n")
    
    # regex to match Phase_XX folders
    phase_pattern = re.compile(r"^Phase_(\d+)_")
    
    # 1. Collect and filter folders
    tasks = []
    if not os.path.exists(base_path):
        print(f"Error: Base path not found: {base_path}")
        say(f"Error: Base path not found:")
        return

    for item in os.listdir(base_path):
        full_path = os.path.join(base_path, item)
        if os.path.isdir(full_path):
            match = phase_pattern.match(item)
            if match:
                phase_num = int(match.group(1))
                if phase_num >= 48:
                    tasks.append((phase_num, full_path, item))
    
    # 2. Sort by phase number
    tasks.sort(key=lambda x: x[0])
    
    print(f"Found {len(tasks)} phases to process starting from Phase 45.")
    # 3. Execution Loop
    for i, (phase_num, folder_path, folder_name) in enumerate(tasks):
        prompt_file = os.path.join(folder_path, "Prompt.md")
        
        # Verify prompt file exists (optional, but good for safety)
        if not os.path.exists(prompt_file):
            print(f"[{time.strftime('%H:%M:%S')}] Warning: Prompt file not found for {folder_name}, skipping.")
            continue

        say(f"Processing Phase {phase_num}")
        # Construct the prompt string exactly as requested
        # Note: We use the absolute path for the prompt file
        with open(prompt_file, 'r', encoding='utf-8') as f:
            prompt_content = f.read().strip()

        gemini_prompt = f"{prompt_content}. Strictly follow the Prompt. After every search, reflect upon it and the next search must be deepening the previous search."
        
        # print(gemini_prompt)
        print(f"\n{'='*60}")
        print(f"Processing: {folder_name} (Phase {phase_num})")
        print(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*60}\n")

        cmd = [
            "gemini", 
            "--prompt", gemini_prompt, 
            "--yolo", 
            "--output-format", "stream-json"
        ]
        
        try:
            # Execute command and stream output
            # We use Popen to stream stdout in real-time
            process = subprocess.Popen(
                cmd, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE, 
                text=True, 
                encoding='utf-8',
                cwd=base_path # Execute from base path context, though absolute paths are used
            )
            
            # Read stdout line by line
            if process.stdout:
                for line in process.stdout:
                    try:
                        # Parse the JSON line
                        data = json.loads(line)
                        msg_type = data.get("type")
                        
                        # Handle different message types for cleaner output
                        if msg_type == "message":
                            content = data.get("content", "")
                            if content:
                                print(content, end="", flush=True)
                        elif msg_type == "tool_use":
                            tool_name = data.get("tool_name", "Unknown")
                            tool_args = data.get("parameters", {})
                            # Format tool args nicely if possible
                            args_str = json.dumps(tool_args)
                            if len(args_str) > 100:
                                args_str = args_str[:100] + "..."
                            print(f"\n\n> [Tool Use] {tool_name}: {args_str}", flush=True)
                        elif msg_type == "tool_result":
                            status = data.get("status", "Unknown")
                            output = data.get("output", "")
                            # Truncate output for log readability
                            out_preview = output[:200].replace("\n", " ") + "..." if len(output) > 200 else output.replace("\n", " ")
                            print(f"\n> [Tool Result] {status}: {out_preview}\n", flush=True)
                        elif msg_type == "error":
                            error = data.get("error", "Unknown")
                            print(f"\n> [Error] {error}\n", flush=True)
                            
                    except json.JSONDecodeError:
                        # If line is not JSON, print it as raw text
                        print(line, end="", flush=True)
            
            # Wait for completion
            return_code = process.wait()
            
            if return_code != 0:
                stderr = process.stderr.read() if process.stderr else ""
                print(f"\nError executing phase {phase_num}. Exit code: {return_code}")
                say(f"\nError executing phase {phase_num}. Exit code: {return_code}")
                print(f"Stderr: {stderr}")
            else:
                print(f"\n[Success] Phase {phase_num} completed.")
                say(f"\n[Success] Phase {phase_num} completed.")

        except Exception as e:
            print(f"\nException occurred during execution: {e}")

        # Wait 30 minutes before the next task (except after the last one)
        if i < len(tasks) - 1:
            wait_minutes = 0.5
            print(f"\nWaiting {wait_minutes} minutes before next phase...")
            time.sleep(wait_minutes * 60)
        else:
            print("\nAll tasks completed.")

if __name__ == "__main__":
    main()
