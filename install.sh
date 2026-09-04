#!/bin/sh

set -e

REPO="https://raw.githubusercontent.com/n0tpurplx/Purplecli/main"
INSTALL_DIR="$HOME/.local/bin"
INSTALL_FILE="$INSTALL_DIR/PurpleCli"

echo "Installing PurpleCli..."
echo ""

if ! command -v python3 >/dev/null 2>&1; then
    echo "Error: python3 is required but was not found."
    exit 1
fi

if ! command -v curl >/dev/null 2>&1; then
    echo "Error: curl is required but was not found."
    exit 1
fi

mkdir -p "$INSTALL_DIR"

curl -fsSL "$REPO/PurpleCli.py" -o "$INSTALL_FILE"

chmod +x "$INSTALL_FILE"

case ":$PATH:" in
    *":$INSTALL_DIR:"*)
        ;;
    *)
        echo "Adding $INSTALL_DIR to PATH..."

        SHELL_NAME=$(basename "${SHELL:-sh}")

        if [ "$SHELL_NAME" = "fish" ]; then
            fish -c "set -U fish_user_paths $INSTALL_DIR \$fish_user_paths"
        else
            PROFILE="$HOME/.profile"

            if [ -f "$PROFILE" ]; then
                if ! grep -q "$INSTALL_DIR" "$PROFILE"; then
                    echo "export PATH=\"\$HOME/.local/bin:\$PATH\"" >> "$PROFILE"
                fi
            else
                echo "export PATH=\"\$HOME/.local/bin:\$PATH\"" > "$PROFILE"
            fi
        fi

        ;;
esac

echo ""
echo "✓ PurpleCli installed."
echo "✓ OpenRouter supported."
echo "✓ Google Gemini supported."
echo "✓ OpenAI supported."
echo ""
echo "Run:"
echo "  PurpleCli --setup"
echo ""
