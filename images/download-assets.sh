#!/usr/bin/env bash
# Download the real Sharpe's current-site assets into this folder.
# Run from anywhere:  bash assets/images/download-assets.sh
# After it finishes, set USE_REMOTE_ASSETS = False in build.py and re-run: python3 pages.py
set -euo pipefail
cd "$(dirname "$0")"

dl () { echo "→ $2"; curl -fsSL -A "Mozilla/5.0" "$1" -o "$2"; }

B="https://www.sharpessepticandwelldrilling.com/wp-content/uploads"
dl "$B/2025/08/Sharpes-add-LLC.png"        "sharpes-logo-current.png"
dl "$B/2019/07/banner-home.jpg"            "sharpes-home-banner.jpg"
dl "$B/2025/06/BestofLex_Logo2025-1.png"   "bestoflex-2025.png"
dl "https://www.sharpessepticandwelldrilling.com/wp-content/themes/splashomnimediatheme/images/img-004.jpg" "sharpes-about-trust.jpg"
dl "$B/2019/07/child-header1.jpg"          "sharpes-septic-team.jpg"
dl "$B/2019/07/child-header-3.jpg"         "sharpes-well-frontyard.jpg"
dl "$B/2019/07/tools-closeup.jpg"          "sharpes-well-tools.jpg"
dl "$B/2019/07/child-header-2.jpg"         "sharpes-grease-digging.jpg"
dl "$B/2019/07/backing-up.jpg"             "sharpes-grease-backing-up.jpg"
dl "$B/2019/07/child-header-4.jpg"         "sharpes-precast-frontyard.jpg"

echo "Done. All assets saved to $(pwd)"
