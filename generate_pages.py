import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Fix links in index.html
html = html.replace('<li class="nav-item"><a class="nav-link active" href="#">Anasayfa</a></li>', 
                    '<li class="nav-item"><a class="nav-link active" href="index.html">Anasayfa</a></li>\n                    <li class="nav-item"><a class="nav-link" href="hakkimizda.html">Hakkımızda</a></li>')

html = html.replace('<li><a class="dropdown-item" href="#">Fakülteler</a></li>', '<li><a class="dropdown-item" href="programlar.html">Fakülteler</a></li>')
html = html.replace('<li><a class="dropdown-item" href="#">Enstitüler</a></li>', '<li><a class="dropdown-item" href="programlar.html">Enstitüler</a></li>')
html = html.replace('<li><a class="dropdown-item" href="#">Yüksekokullar</a></li>', '<li><a class="dropdown-item" href="programlar.html">Yüksekokullar</a></li>')

html = html.replace('<li class="nav-item"><a class="nav-link" href="#">İletişim</a></li>', '<li class="nav-item"><a class="nav-link" href="iletisim.html">İletişim</a></li>')

html = html.replace('<a href="#academics" class="btn btn-warning hero-btn me-3 smooth-scroll">Programları İncele</a>', '<a href="programlar.html" class="btn btn-warning hero-btn me-3">Programları İncele</a>')

html = re.sub(r'<button class="btn btn-outline-primary btn-lg mt-2" type="button" data-bs-toggle="collapse" data-bs-target="#moreAbout".*?</div>\s+</div>', '<a href="hakkimizda.html" class="btn btn-outline-primary btn-lg mt-2">Daha Fazla Bilgi</a>', html, flags=re.DOTALL)

html = html.replace('<button type="button" class="btn btn-primary btn-lg" onclick="alert(\'Tüm akademik programların listelendiği detaylı sayfaya geçiş yapılıyor.\')">Tüm Programları Görüntüle</button>', '<a href="programlar.html" class="btn btn-primary btn-lg">Tüm Programları Görüntüle</a>')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

# Extract sections
header_match = re.search(r'(<!-- Top Bar -->.*?</nav>)', html, re.DOTALL)
header = header_match.group(1) if header_match else ""
# Remove "active" from header links
header = header.replace('class="nav-link active"', 'class="nav-link"')

footer_match = re.search(r'(<!-- Footer -->.*?</footer>)', html, re.DOTALL)
footer = footer_match.group(1) if footer_match else ""

modals_match = re.search(r'(<!-- Login Modal -->.*?</script>)', html, re.DOTALL)
modals = modals_match.group(1) if modals_match else ""


def make_page(title, body_content, active_link):
    page_header = header.replace(f'href="{active_link}" class="nav-link"', f'href="{active_link}" class="nav-link active"')
    
    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Akademi Üniversitesi</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
    <style>
        .page-hero {{
            background: linear-gradient(rgba(10, 25, 47, 0.85), rgba(10, 25, 47, 0.85)), url('https://images.unsplash.com/photo-1541339907198-e08756ebafe3?ixlib=rb-1.2.1&auto=format&fit=crop&w=1920&q=80') center/cover;
            padding: 80px 0;
            color: white;
            text-align: center;
        }}
    </style>
</head>
<body>
{page_header}
{body_content}
{footer}
{modals}
<script src="js/main.js"></script>
</body>
</html>"""

hakkimizda_body = """
<div class="page-hero">
    <div class="container">
        <h1 class="display-4 fw-bold text-warning">Hakkımızda</h1>
        <p class="lead">Köklü Tarihimiz ve Yenilikçi Vizyonumuz</p>
    </div>
</div>
<div class="container py-5 my-4">
    <div class="row align-items-center mb-5">
        <div class="col-md-6">
            <img src="https://images.unsplash.com/photo-1523050854058-8df90110c9f1?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" class="img-fluid rounded shadow-lg" alt="Tarihçe">
        </div>
        <div class="col-md-6 ps-lg-5 mt-4 mt-md-0">
            <h6 class="text-warning fw-bold text-uppercase">Tarihçe</h6>
            <h2 class="section-title mb-4">Dünden Bugüne Akademi</h2>
            <p class="lead">Üniversitemiz, yarım asrı aşkın bir süredir akademik mükemmellik hedefiyle yoluna devam etmektedir.</p>
            <p class="text-muted">Eğitim ve araştırma odaklı vizyonumuz sayesinde sadece yerel değil, küresel ölçekte de söz sahibi bilim insanları ve liderler yetiştiriyoruz. Sürdürülebilir kampüsümüz ve teknolojik altyapımız ile öğrencilerimize eşsiz bir deneyim sunuyoruz.</p>
        </div>
    </div>
    <div class="row text-center mt-5 pt-4 border-top">
        <div class="col-md-4 mb-4">
            <div class="p-4 border rounded shadow-sm h-100 bg-white">
                <i class="fas fa-bullseye fa-3x text-warning mb-3"></i>
                <h4 class="fw-bold text-primary">Misyonumuz</h4>
                <p class="text-muted mt-3">Bilimsel düşünceyi rehber edinerek uluslararası standartlarda, etik değerlere bağlı, yenilikçi eğitim vermek ve topluma fayda sağlamak.</p>
            </div>
        </div>
        <div class="col-md-4 mb-4">
            <div class="p-4 border rounded shadow-sm h-100 bg-white">
                <i class="fas fa-eye fa-3x text-warning mb-3"></i>
                <h4 class="fw-bold text-primary">Vizyonumuz</h4>
                <p class="text-muted mt-3">Dünyanın en prestijli ilk 500 üniversitesi arasında kalıcı olarak yer almak ve araştırma çıktılarıyla insanlığa yön vermek.</p>
            </div>
        </div>
        <div class="col-md-4 mb-4">
            <div class="p-4 border rounded shadow-sm h-100 bg-white">
                <i class="fas fa-handshake fa-3x text-warning mb-3"></i>
                <h4 class="fw-bold text-primary">Değerlerimiz</h4>
                <p class="text-muted mt-3">Şeffaflık, evrensel etik değerlere sıkı sıkıya bağlılık, yenilikçilik, liyakat ve fırsat eşitliği sunmak.</p>
            </div>
        </div>
    </div>
</div>
"""

programlar_body = """
<div class="page-hero" style="background-image: linear-gradient(rgba(10, 25, 47, 0.85), rgba(10, 25, 47, 0.85)), url('https://images.unsplash.com/photo-1532094349884-543bc11b234d?ixlib=rb-1.2.1&auto=format&fit=crop&w=1920&q=80');">
    <div class="container">
        <h1 class="display-4 fw-bold text-warning">Akademik Programlar</h1>
        <p class="lead">Geleceğinizi Şekillendirecek Geniş Yelpaze</p>
    </div>
</div>
<div class="container py-5 my-4">
    <div class="row g-4">
        <div class="col-lg-4 col-md-6">
            <div class="faculty-card shadow-sm border-0 bg-white p-4 text-center rounded">
                <i class="fas fa-laptop-code fa-3x text-warning mb-3"></i>
                <h4 class="text-primary fw-bold">Mühendislik Fakültesi</h4>
                <ul class="text-start mt-3 text-muted">
                    <li>Bilgisayar Mühendisliği</li>
                    <li>Elektrik-Elektronik Mühendisliği</li>
                    <li>Makine Mühendisliği</li>
                </ul>
                <button class="btn btn-outline-primary mt-3 w-100">Detaylı Bilgi</button>
            </div>
        </div>
        <div class="col-lg-4 col-md-6">
            <div class="faculty-card shadow-sm border-0 bg-white p-4 text-center rounded">
                <i class="fas fa-heartbeat fa-3x text-warning mb-3"></i>
                <h4 class="text-primary fw-bold">Tıp Fakültesi</h4>
                <ul class="text-start mt-3 text-muted">
                    <li>Temel Tıp Bilimleri</li>
                    <li>Dahili Tıp Bilimleri</li>
                    <li>Cerrahi Tıp Bilimleri</li>
                </ul>
                <button class="btn btn-outline-primary mt-3 w-100">Detaylı Bilgi</button>
            </div>
        </div>
        <div class="col-lg-4 col-md-6">
            <div class="faculty-card shadow-sm border-0 bg-white p-4 text-center rounded">
                <i class="fas fa-balance-scale fa-3x text-warning mb-3"></i>
                <h4 class="text-primary fw-bold">Hukuk Fakültesi</h4>
                <ul class="text-start mt-3 text-muted">
                    <li>Kamu Hukuku</li>
                    <li>Özel Hukuk</li>
                    <li>Uluslararası Hukuk</li>
                </ul>
                <button class="btn btn-outline-primary mt-3 w-100">Detaylı Bilgi</button>
            </div>
        </div>
        <div class="col-lg-4 col-md-6">
            <div class="faculty-card shadow-sm border-0 bg-white p-4 text-center rounded">
                <i class="fas fa-paint-brush fa-3x text-warning mb-3"></i>
                <h4 class="text-primary fw-bold">Güzel Sanatlar Fakültesi</h4>
                <ul class="text-start mt-3 text-muted">
                    <li>Grafik Tasarım</li>
                    <li>İç Mimarlık ve Çevre Tasarımı</li>
                    <li>Endüstriyel Tasarım</li>
                </ul>
                <button class="btn btn-outline-primary mt-3 w-100">Detaylı Bilgi</button>
            </div>
        </div>
        <div class="col-lg-4 col-md-6">
            <div class="faculty-card shadow-sm border-0 bg-white p-4 text-center rounded">
                <i class="fas fa-atom fa-3x text-warning mb-3"></i>
                <h4 class="text-primary fw-bold">Fen-Edebiyat Fakültesi</h4>
                <ul class="text-start mt-3 text-muted">
                    <li>Matematik ve Bilgisayar Bilimleri</li>
                    <li>Moleküler Biyoloji ve Genetik</li>
                    <li>Psikoloji</li>
                </ul>
                <button class="btn btn-outline-primary mt-3 w-100">Detaylı Bilgi</button>
            </div>
        </div>
        <div class="col-lg-4 col-md-6">
            <div class="faculty-card shadow-sm border-0 bg-white p-4 text-center rounded">
                <i class="fas fa-chart-line fa-3x text-warning mb-3"></i>
                <h4 class="text-primary fw-bold">İşletme Fakültesi</h4>
                <ul class="text-start mt-3 text-muted">
                    <li>İşletme Yönetimi</li>
                    <li>Ekonomi ve Finans</li>
                    <li>Uluslararası Ticaret</li>
                </ul>
                <button class="btn btn-outline-primary mt-3 w-100">Detaylı Bilgi</button>
            </div>
        </div>
    </div>
</div>
"""

iletisim_body = """
<div class="page-hero" style="background-image: linear-gradient(rgba(10, 25, 47, 0.85), rgba(10, 25, 47, 0.85)), url('https://images.unsplash.com/photo-1519452314548-5c4dff48fbbe?ixlib=rb-1.2.1&auto=format&fit=crop&w=1920&q=80');">
    <div class="container">
        <h1 class="display-4 fw-bold text-warning">İletişim</h1>
        <p class="lead">Bize Ulaşın, Sorularınızı Yanıtlayalım</p>
    </div>
</div>
<div class="container py-5 my-4">
    <div class="row g-5">
        <div class="col-lg-6">
            <div class="bg-white p-5 rounded shadow-sm border">
                <h3 class="fw-bold text-primary mb-4">Mesaj Gönderin</h3>
                <form onsubmit="event.preventDefault(); alert('Mesajınız başarıyla iletildi!'); this.reset();">
                    <div class="mb-3">
                        <label class="form-label text-muted">Adınız Soyadınız</label>
                        <input type="text" class="form-control" required>
                    </div>
                    <div class="mb-3">
                        <label class="form-label text-muted">E-Posta Adresiniz</label>
                        <input type="email" class="form-control" required>
                    </div>
                    <div class="mb-3">
                        <label class="form-label text-muted">Konu</label>
                        <select class="form-select">
                            <option>Genel Bilgi Talebi</option>
                            <option>Öğrenci İşleri</option>
                            <option>Teknik Destek</option>
                            <option>Öneri / Şikayet</option>
                        </select>
                    </div>
                    <div class="mb-4">
                        <label class="form-label text-muted">Mesajınız</label>
                        <textarea class="form-control" rows="5" required></textarea>
                    </div>
                    <button type="submit" class="btn btn-warning w-100 fw-bold py-2">Mesajı Gönder</button>
                </form>
            </div>
        </div>
        <div class="col-lg-6">
            <h3 class="fw-bold text-primary mb-4">İletişim Bilgilerimiz</h3>
            <div class="d-flex mb-4 p-3 border rounded bg-light">
                <div class="bg-white p-3 rounded shadow-sm me-4 d-flex align-items-center justify-content-center" style="width: 60px; height: 60px;">
                    <i class="fas fa-map-marker-alt fa-2x text-warning"></i>
                </div>
                <div>
                    <h5 class="fw-bold text-primary">Merkez Kampüs</h5>
                    <p class="text-muted mb-0">Üniversite Cad. No:1 Kampüs, Merkez / Türkiye</p>
                </div>
            </div>
            <div class="d-flex mb-4 p-3 border rounded bg-light">
                <div class="bg-white p-3 rounded shadow-sm me-4 d-flex align-items-center justify-content-center" style="width: 60px; height: 60px;">
                    <i class="fas fa-phone-alt fa-2x text-warning"></i>
                </div>
                <div>
                    <h5 class="fw-bold text-primary">Telefon</h5>
                    <p class="text-muted mb-0">+90 (212) 555 00 00<br>+90 (212) 555 00 01 (Faks)</p>
                </div>
            </div>
            <div class="d-flex mb-4 p-3 border rounded bg-light">
                <div class="bg-white p-3 rounded shadow-sm me-4 d-flex align-items-center justify-content-center" style="width: 60px; height: 60px;">
                    <i class="fas fa-envelope fa-2x text-warning"></i>
                </div>
                <div>
                    <h5 class="fw-bold text-primary">E-Posta</h5>
                    <p class="text-muted mb-0">info@akademi.edu.tr<br>destek@akademi.edu.tr</p>
                </div>
            </div>
            
            <!-- Map Placeholder -->
            <div class="ratio ratio-21x9 mt-4 rounded overflow-hidden shadow-sm">
                <div class="bg-secondary d-flex align-items-center justify-content-center text-white" style="background: url('https://images.unsplash.com/photo-1524661135-423995f22d0b?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80') center/cover;">
                    <div style="position:absolute; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.5);"></div>
                    <div style="z-index:1; text-align:center;">
                        <i class="fas fa-map-marked-alt fa-3x text-warning mb-2"></i>
                        <h5 class="fw-bold">Haritada Görüntüle</h5>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
"""

with open("hakkimizda.html", "w", encoding="utf-8") as f:
    f.write(make_page("Hakkımızda", hakkimizda_body, "hakkimizda.html"))

with open("programlar.html", "w", encoding="utf-8") as f:
    f.write(make_page("Akademik Programlar", programlar_body, "programlar.html"))

with open("iletisim.html", "w", encoding="utf-8") as f:
    f.write(make_page("İletişim", iletisim_body, "iletisim.html"))

