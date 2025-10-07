#!/bin/bash
set -e

# Default model
MODEL="gpt-5"

# Parse model argument if provided
while [[ $# -gt 0 ]]; do
    case $1 in
        --model)
            MODEL="$2"
            shift 2
            ;;
        *)
            break
            ;;
    esac
done

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}🚀 Setting up environment and running render_prompts.py${NC}"

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo -e "${YELLOW}📦 Creating virtual environment...${NC}"
    python3 -m venv .venv
fi

# Activate virtual environment
echo -e "${YELLOW}🔌 Activating virtual environment...${NC}"
source .venv/bin/activate

# Install dependencies from requirements.txt 
echo -e "${YELLOW}📋 Installing dependencies from requirements.txt...${NC}"
uv pip install -r requirements.txt


# Run render_prompts.py with all passed arguments
echo -e "${YELLOW}🎯 Running render_prompts.py...${NC}"
python render_prompts.py "$@"

echo -e "${GREEN}✅ Script completed successfully!${NC}"

# Run Copilot CLI
echo -e "${YELLOW}🤖 Running Copilot CLI with model: ${MODEL}${NC}"
copilot --model "$MODEL" --add-dir . --allow-all-tools -p "Complete the task in the coordinator.md."
 
