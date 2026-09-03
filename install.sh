#!/bin/sh

set -e

REPO="https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main"
INSTALL_DIR="$HOME/.local/bin"

echo "Installing PurpleCli..."

mkdir -p "$INSTALL_DIR"

curl -fsSL "$REPO/PurpleCli.py" -o "$INSTALL_DIR/PurpleCli"

chmod +x "$INSTALL_DIR/PurpleCli"

# Check whether ~/.local/bin is already in PATH
case ":$PATH:" in
    *":$INSTALL_DIR:"*)
        ;;
    *)
        echo ""
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
echo ""
echo "Run:"
echo "  PurpleCli --setup"
echo ""
