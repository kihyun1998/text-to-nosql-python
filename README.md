# text-to-nosql-python

Text-to-NoSQL Project with Python


## 가상환경 생성하기

```bash
# Windows
python -m venv myenv

# macOS/Linux
python3 -m venv myenv
```

## 가상환경 활성화하기
```bash
# Windows (PowerShell)
.\myenv\Scripts\Activate.ps1
.\myenv_home\Scripts\Activate.ps1

# Windows (CMD)
myenv\Scripts\activate

# macOS/Linux
source myenv/bin/activate
```
활성화되면 터미널 프롬프트 앞에 (myenv)가 표시됩니다.

## 가상환경 비활성화하기
```bash
deactivate
```

## requirements.txt 관리하기

### requirements.txt 생성하기
현재 환경에 설치된 모든 패키지를 requirements.txt 파일로 저장:
```bash
pip freeze > requirements.txt
```

### requirements.txt로 패키지 설치하기
```bash
pip install -r requirements.txt
```

## 주요 명령어 정리
- 패키지 설치: `pip install 패키지명`
- 설치된 패키지 목록 확인: `pip list`
- 특정 버전 설치: `pip install 패키지명==버전`
- 패키지 업그레이드: `pip install --upgrade 패키지명`

## 팁
1. 프로젝트마다 별도의 가상환경을 만들어 사용하는 것을 권장합니다.
2. requirements.txt는 프로젝트의 루트 디렉토리에 저장하는 것이 관례입니다.
3. .gitignore 파일에 가상환경 디렉토리(myenv/)를 추가하는 것을 잊지 마세요.