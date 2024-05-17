generate_qr_code() {
    local url=$1
    python3 -c "
import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('$url')
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('ngrok_qr.png')
"
    echo "QR code saved as ngrok_qr.png"
}

osascript <<EOF
tell application "Terminal"
    do script "source activate ml && cd \"/Users/tanmay/Documents/GitHub/anime-gan/\" && python app.py && echo 'Python app is running' && exec bash"
end tell
EOF

sleep 5

osascript <<EOF
tell application "Terminal"
    do script "ngrok http 5000 && echo 'ngrok is running' && exec bash"
end tell
EOF

sleep 10

NGROK_URL=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | jq -r '.tunnels[0].public_url')

if [ -z "$NGROK_URL" ]; then
    echo "ngrok URL could not be retrieved. Make sure ngrok is running."
    exit 1
fi

echo "ngrok URL: $NGROK_URL"

generate_qr_code $NGROK_URL

open ngrok_qr.png

echo "Script execution complete."
!/bin/bash