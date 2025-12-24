import subprocess
import sys
import os

requset_path = os.path.join(os.path.dirname(__file__), "./requirements.txt")
def install_requirements():
    try:
        # Prüfen, ob alle Abhängigkeiten installiert sind
        with open(requset_path, 'r') as f:
            requirements = f.read().splitlines()
        
        for requirement in requirements:
            try:
                # Reinen Paketnamen extrahieren (ohne Version/Sonderzeichen)
                package_name = requirement.split('==')[0].split('>')[0].split('<')[0].split('~')[0].strip()
                # print(f"{package_name} EN_TEXT...")
                if package_name == 'uuid7':
                    from uuid_extensions import uuid7
                else:
                    __import__(package_name)
            except ImportError:
                print(f"{requirement} Nicht installiert, wird installiert...")
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', requirement])
        
        print("WeiLin-Comfyui-Tools ==> Alle Abhängigkeiten sind installiert。")
    except Exception as e:
        print(f"WeiLin-Comfyui-Tools ==> EN_TEXT: {e}")