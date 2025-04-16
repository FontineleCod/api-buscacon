from scraper import buscar_concursos_por_estado

def main():
    print("🧭 Busca de Concursos por Estado (PCI Concursos)")
    estado = input("Digite a sigla do estado (ex: PA, SP, RN): ").upper()

    print(f"\n🔍 Buscando concursos abertos para {estado}...\n")
    concursos = buscar_concursos_por_estado(estado)

    if concursos:
        for i, (titulo, link, detalhes) in enumerate(concursos, 1):
            print(f"{i}. 📌 {titulo}")
            print(f"   🔗 {link}")
            print(f"   📋 Detalhes: {detalhes}")
            print("-" * 60)
    else:
        print("❌ Nenhum concurso encontrado para esse estado.")
        print("Nenhum concurso encontrado ou erro na busca.\n")

if __name__ == "__main__":
    main()
