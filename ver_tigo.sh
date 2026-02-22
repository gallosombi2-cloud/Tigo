#!/bin/bash
echo "[*] Obteniendo token de Tigo Sports..."
URL=$(python3 fetcher.py)
echo "[+] Conectando a: $URL"
mpv --profile=low-latency --user-agent="Mozilla/5.0" "$URL"
