## 使用方法

### 安裝依賴
```bash
pip install -r requirements.txt
```

### Data Link Layer 實驗
以管理員身分執行:
```bash
python raw.py "<介面卡名稱>" <目標 MAC 地址>
```

Wireshark 過濾建議使用:
```bash
eth.dst == <目標 MAC>
```

### Network Layer 實驗
以管理員身分執行:
```bash
python ip.py <目標 IP 地址>
```

Wireshark 過濾建議使用:
```bash
ip.dst == <目標公用 IP>
```

## GitHub 使用方法

### 修改前
```bash
git pull origin main
```

### 修改後
```bash
git add .
git commit -m "message"
git push origin main
```