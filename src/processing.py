
from typing import List, Dict, Any
from collections import Counter

def clean_rows(rows: List[Dict[str, str]]) -> List[Dict[str, Any]]:
    """
    - age boş veya sayısal değilse satırı atar
    - age'i int'e çevirir
    - name ve city için strip() uygular
    """
    cleaned = []
    for r in rows:
        # Güvenlik: beklenmeyen anahtar isimleri varsa hata yerine atla/uygun işle
        name = r.get("name", "")
        age = r.get("age", "")
        city = r.get("city", "")

        if age is None:
            continue
        age_str = str(age).strip()
        if age_str == "":
            continue
        # Sayısal mı kontrol et
        if not age_str.isdigit():
            # Bazı CSV'lerde yaş ondalık veya boşluk içerebilir; int dönüşümü dene:
            try:
                age_val = int(float(age_str))
            except Exception:
                continue
        else:
            age_val = int(age_str)

        cleaned.append({
            "name": str(name).strip(),
            "age": age_val,
            "city": str(city).strip()
        })
    return cleaned

def stats(rows: List[Dict[str, str]]) -> Dict[str, Any]:
    
    cleaned = clean_rows(rows)
    count = len(cleaned)
    if count == 0:
        avg_age = None
    else:
        total_age = sum(r["age"] for r in cleaned)
        avg_age = round(total_age / count, 2)
    by_city = Counter()
    for r in cleaned:
        by_city[r["city"]] += 1

    return {
        "count": count,
        "avg_age": avg_age,
        "by_city": dict(by_city),
        "cleaned": cleaned
    }

def build_report(st: Dict[str, Any]) -> str:
    lines = []
    lines.append("RAPOR")
    lines.append("======================")
    lines.append(f"Geçerli kayıt sayısı: {st.get('count', 0)}")
    avg = st.get("avg_age")
    lines.append(f"Ortalama yaş: {avg if avg is not None else 'N/A'}")
    lines.append("")
    lines.append("Şehir dağılımı:")
    by_city = st.get("by_city", {})
    if not by_city:
        lines.append("  (kayıt yok)")
    else:
        for city, n in by_city.items():
            lines.append(f"  {city}: {n}")
    lines.append("======================")
    return "\n".join(lines) + "\n"
