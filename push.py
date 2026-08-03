import subprocess
import sys

def executar_git():
    mensagem = input("Digite a mensagem do commit: ").strip()
    branch = input("Digite o nome da branch: ").strip()

    if not mensagem or not branch:
        print("Erro: A mensagem e a branch não podem estar vazias.")
        sys.exit(1)

    comandos = [
        ["git", "add", "."],
        ["git", "commit", "-m", mensagem],
        ["git", "push", "origin", branch]
    ]

    for comando in comandos:
        print(f"\n---> Executando: {' '.join(comando)}")
        resultado = subprocess.run(comando)
        
        if resultado.returncode != 0:
            print(f"\n❌ Erro ao executar o comando: {' '.join(comando)}")
            sys.exit(resultado.returncode)

    print("\n✅ Sucesso! Código adicionado, commitado e enviado.")

if __name__ == "__main__":
    executar_git()