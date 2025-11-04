
from src.dosya_islemleri import read_csv, write_json, write_text
from src.processing import stats, build_report

def main():
    read_doc = "C:/Users/rabia/OneDrive/Masaüstü/Betiködev/betik_diller/exercise/data/people.csv"
    write_stats = "C:/Users/rabia/OneDrive/Masaüstü/Betiködev/betik_diller/exercise/data/stats.json"
    write_cleaned = "C:/Users/rabia/OneDrive/Masaüstü/Betiködev/betik_diller/exercise/data/cleaned.json"
    write_txt = "C:/Users/rabia/OneDrive/Masaüstü/Betiködev/betik_diller/exercise/data/stats_txt.txt"

    # Oku
    rows = read_csv(read_doc)

    # İstatistik üret (içinde temizleme de var)
    st = stats(rows)

    # İstatistikleri yaz
    write_json(write_stats, {
        "count": st["count"],
        "avg_age": st["avg_age"],
        "by_city": st["by_city"],
    })

    # Temizlenmiş kayıtları da ayrı JSON olarak kaydet
    write_json(write_cleaned, st["cleaned"])

    # Kısa raporı txt olarak kaydet
    write_text(write_txt, build_report(st))

    print("bitti")

if __name__ == "__main__":
    main()

    
    
    
   