@echo off
setlocal

REM ===== PEGAR NOME DA PASTA (PROJETO) =====
for %%I in (.) do set PROJETO=%%~nxI

REM ===== PERGUNTAR AO USUARIO =====
echo Nome detectado da pasta: %PROJETO%
set /p CONFIRMA="Usar este nome como projeto? (S/N): "

if /I "%CONFIRMA%"=="N" (
    set /p PROJETO="Digite o nome correto do projeto: "
)

REM ===== CONFIGURACOES =====
set BRANCH=main
set REMOTE=origin
set COMMIT_MSG=Atualizacao automatica

REM ===== URL DO REPOSITORIO =====
set REPO_URL=https://github.com/davigopi/%PROJETO%.git

REM ===== CONFIGURAR USUARIO GLOBAL =====
git config --global user.name "davigopi"
git config --global user.email "davigopi@gmail.com"

echo Projeto final: %PROJETO%
echo Repositorio: %REPO_URL%
echo.

REM ===== VERIFICAR SE E UM REPOSITORIO GIT =====
if not exist ".git" (
    echo Repositorio Git nao encontrado. Inicializando...
    git init
    git checkout -B %BRANCH%
    git remote add %REMOTE% %REPO_URL%
) else (
    REM ===== VERIFICAR SE REMOTE EXISTE =====
    git remote get-url %REMOTE% >nul 2>&1
    if errorlevel 1 (
        echo Adicionando remoto %REMOTE%...
        git remote add %REMOTE% %REPO_URL%
    ) else (
        echo Atualizando URL do remoto %REMOTE%...
        git remote set-url %REMOTE% %REPO_URL%
    )
)

REM ===== STATUS =====
git status

REM ===== ADICIONAR ARQUIVOS =====
git add .

REM ===== COMMIT =====
git commit -m "%COMMIT_MSG%" || echo Nenhuma alteracao para commit

REM ===== PUSH =====
git push -u %REMOTE% %BRANCH%

echo.
echo ✔ Upload concluido com sucesso!
pause
