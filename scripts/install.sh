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