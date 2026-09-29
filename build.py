# -*- coding: utf-8 -*-
"""Genera las páginas estáticas de spacetorise.com a partir de partials + contenido."""
import os, json, html

OUT = os.path.dirname(os.path.abspath(__file__))
WA = "https://wa.me/573107503359?text=" + "Hola!%20Quiero%20reservar%20mi%20cita%20%F0%9F%98%8A"
IMG = "/assets/img/"

NAV = [("RTT", "/rtt/"), ("Heal / Rise / Shine", "/heal-rise-shine/"), ("Kids", "/kids/"),
       ("Coaching", "/coaching/"), ("Gong", "/gong/"), ("Shop", "/shop/")]

SVG_WA = '<svg viewBox="0 0 24 24"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.4-.5.3-.5c.1-.2 0-.4 0-.5L9.1 6.9c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.2-.3-.3-.6-.4zM12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.5 0-3-.4-4.3-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2z"/></svg>'
SVG_CART = '<svg viewBox="0 0 24 24"><path d="M3 4h2l2.4 11.2a1 1 0 0 0 1 .8h8.8a1 1 0 0 0 1-.8L20 8H6.5"/><circle cx="9.5" cy="20" r="1.2"/><circle cx="17" cy="20" r="1.2"/></svg>'
SVG_IG = '<svg viewBox="0 0 24 24"><path d="M12 7.3a4.7 4.7 0 1 0 0 9.4 4.7 4.7 0 0 0 0-9.4zm0 7.7a3 3 0 1 1 0-6 3 3 0 0 1 0 6zm5-8a1.1 1.1 0 1 1-2.2 0 1.1 1.1 0 0 1 2.2 0zM21 8.6c-.1-1.5-.4-2.8-1.5-3.9S17 3.3 15.4 3.2c-1.6-.1-6.2-.1-7.8 0C6.1 3.3 4.8 3.6 3.7 4.7S2.3 7.1 2.2 8.6c-.1 1.6-.1 6.2 0 7.8.1 1.5.4 2.8 1.5 3.9s2.4 1.4 3.9 1.5c1.6.1 6.2.1 7.8 0 1.5-.1 2.8-.4 3.9-1.5s1.4-2.4 1.5-3.9c.1-1.6.1-6.2 0-7.8zm-2 9.5a3 3 0 0 1-1.7 1.7c-1.2.5-4 .4-5.3.4s-4.1.1-5.3-.4a3 3 0 0 1-1.7-1.7c-.5-1.2-.4-4-.4-5.3s-.1-4.1.4-5.3A3 3 0 0 1 6.7 5.9c1.2-.5 4-.4 5.3-.4s4.1-.1 5.3.4a3 3 0 0 1 1.7 1.7c.5 1.2.4 4 .4 5.3s.1 4.1-.4 5.3z"/></svg>'
SVG_YT = '<svg viewBox="0 0 24 24"><path d="M23 7.2a2.9 2.9 0 0 0-2-2C19.2 4.7 12 4.7 12 4.7s-7.2 0-9 .5a2.9 2.9 0 0 0-2 2C.5 9 .5 12 .5 12s0 3 .5 4.8a2.9 2.9 0 0 0 2 2c1.8.5 9 .5 9 .5s7.2 0 9-.5a2.9 2.9 0 0 0 2-2c.5-1.8.5-4.8.5-4.8s0-3-.5-4.8zM9.7 15V9l6 3-6 3z"/></svg>'
SVG_FB = '<svg viewBox="0 0 24 24"><path d="M13.5 22v-8h2.7l.4-3.2h-3.1V8.8c0-.9.3-1.6 1.6-1.6h1.7V4.4c-.3 0-1.3-.1-2.4-.1-2.4 0-4.1 1.5-4.1 4.2v2.3H7.5V14h2.8v8h3.2z"/></svg>'
SVG_IN = '<svg viewBox="0 0 24 24"><path d="M6.9 21H3V8.5h3.9V21zM4.9 6.8a2.3 2.3 0 1 1 0-4.6 2.3 2.3 0 0 1 0 4.6zM21 21h-3.9v-6.1c0-1.5 0-3.3-2-3.3s-2.3 1.6-2.3 3.2V21H9V8.5h3.7v1.7h.1c.5-1 1.8-2 3.7-2 3.9 0 4.6 2.6 4.6 5.9V21z"/></svg>'


def head(title, desc, path, dark=False):
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="https://spacetorise.com{path}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="https://spacetorise.com/assets/img/Home-Principal-New.jpg">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_CO">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/img/favicon-32.png">
<link rel="apple-touch-icon" href="/assets/img/favicon-180.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+Bengali:wght@200;300&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/main.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"HealthAndBeautyBusiness","name":"Space to Rise","url":"https://spacetorise.com","telephone":"+57 310 750 3359","image":"https://spacetorise.com/assets/img/Home-Principal-New.jpg","description":"{html.escape(desc)}","founder":{{"@type":"Person","name":"Andrea Zafra"}},"areaServed":"Colombia","sameAs":["https://www.instagram.com/spacetorise/","https://www.youtube.com/@spacetorise","https://www.facebook.com/profile.php?id=61574483459317","https://www.linkedin.com/in/andrea-zafra-5b5bb09"]}}</script>
</head>
<body>
<div class="loader" aria-hidden="true">
  <div class="loader__rings"><span></span><span></span><span></span><span></span><span></span>
    <div class="loader__heart"><img src="{IMG}Icono_Home.png" alt=""></div>
    <div class="loader__word">Space <em>to</em> Rise</div>
  </div>
  <div class="loader__bar"><i></i></div>
</div>
<div class="veil-page" aria-hidden="true"></div>
<header class="header{' on-dark' if dark else ''}">
  <div class="wrap">
    <a class="logo" href="/" aria-label="Space to Rise"><img src="{IMG}LOGO-Color_New.png" alt="Space to Rise"></a>
    <nav class="nav" aria-label="Principal">{''.join(f'<a href="{h}">{t}</a>' for t, h in NAV)}</nav>
    <div class="header__actions">
      <button class="cart-btn" aria-label="Carrito">{SVG_CART}<span class="count">0</span></button>
      <a class="btn" href="{WA}" target="_blank" rel="noopener">Agenda tu cita</a>
      <button class="burger" aria-label="Menú" aria-expanded="false"><span></span><span></span></button>
    </div>
  </div>
</header>
<main>
"""


def foot():
    return f"""</main>
<section class="cta">
  <img src="{IMG}Foto_Home_2.jpg" alt="">
  <div class="wrap">
    <h2 class="rv">Sana, transfórmate y evoluciona en quien estás destinado a ser</h2>
    <p class="rv rv-d1" style="color:rgba(255,255,255,.85);max-width:52ch;margin:0 auto 30px">Empieza con una llamada de 20 minutos sin costo para resolver tus dudas.</p>
    <a class="btn light rv rv-d2" href="{WA}" target="_blank" rel="noopener">Agenda tu cita por WhatsApp</a>
  </div>
</section>
<footer class="footer">
  <div class="wrap">
    <div class="top">
      <div>
        <a class="logo" href="/"><img src="{IMG}LOGO-Color_New.png" alt="Space to Rise"></a>
        <p style="margin:18px 0 0;max-width:36ch;color:rgba(255,255,255,.7)">Journey inward &amp; rise from your heart.<br>Human evolution studio.</p>
        <h5 style="margin-top:28px">Nutre tu alma con nuestro newsletter</h5>
        <form class="news" onsubmit="event.preventDefault();window.open('https://wa.me/573107503359?text='+encodeURIComponent('Hola! Quiero suscribirme al newsletter: '+this.querySelector('input').value),'_blank')">
          <input type="email" placeholder="Tu correo" required aria-label="Tu correo"><button type="submit">Suscríbete</button>
        </form>
        <div class="social">
          <a href="https://www.instagram.com/spacetorise/" target="_blank" rel="noopener" aria-label="Instagram">{SVG_IG}</a>
          <a href="https://www.youtube.com/@spacetorise" target="_blank" rel="noopener" aria-label="YouTube">{SVG_YT}</a>
          <a href="https://www.facebook.com/profile.php?id=61574483459317" target="_blank" rel="noopener" aria-label="Facebook">{SVG_FB}</a>
          <a href="https://www.linkedin.com/in/andrea-zafra-5b5bb09" target="_blank" rel="noopener" aria-label="LinkedIn">{SVG_IN}</a>
        </div>
      </div>
      <div>
        <h5>Terapias</h5>
        <ul><li><a href="/rtt/">¿Qué es RTT?</a></li><li><a href="/heal-rise-shine/">Heal · Rise · Shine</a></li><li><a href="/kids/">Kids</a></li><li><a href="/coaching/">Coaching</a></li><li><a href="/gong/">Baño de Gong</a></li><li><a href="/shop/">Audios de autohipnosis</a></li></ul>
      </div>
      <div>
        <h5>Space to Rise</h5>
        <ul><li><a href="/acerca-de-mi/">Acerca de mí</a></li><li><a href="/mision/">Misión</a></li><li><a href="/gif-for-you/">Gift for you</a></li><li><a href="/preguntas-frecuentes/">Preguntas frecuentes</a></li><li><a href="{WA}" target="_blank" rel="noopener">Agenda tu cita</a></li></ul>
      </div>
    </div>
    <div class="bottom">
      <span class="serif">Al despertar tu mundo, iluminas el mundo.</span>
      <span>© Space to Rise · Andrea Zafra · Bogotá, Colombia</span>
    </div>
  </div>
</footer>

<a class="wa" href="{WA}" target="_blank" rel="noopener" aria-label="Escríbenos por WhatsApp"><span class="ico">{SVG_WA}</span><span class="txt">Agenda tu cita</span></a>

<div class="scrim"></div>
<aside class="drawer" aria-label="Carrito">
  <div class="drawer__head"><h3>Tu carrito</h3><button class="drawer__close btn ghost" style="padding:8px 16px">Cerrar</button></div>
  <div class="drawer__items"></div>
  <div class="drawer__foot">
    <div class="drawer__total"><span>Total</span><b></b></div>
    <button class="btn">Finalizar pedido por WhatsApp</button>
    <small>Te confirmamos el pago (Nequi, transferencia o tarjeta) y recibes tus audios en tu correo.</small>
  </div>
</aside>
<div class="modal" role="dialog" aria-modal="true"><div class="modal__box" style="position:relative"><button class="modal__close" aria-label="Cerrar"></button><div class="modal__img"></div><div class="modal__body"></div></div></div>

<script src="/assets/js/main.js"></script>
<script src="/assets/js/shop.js"></script>
</body>
</html>
"""


def tcard(q, who):
    return f'<figure class="tcard" style="margin:0"><p>{q}</p><cite>{who}</cite></figure>'


def marquee(items, reverse=False):
    cards = ''.join(tcard(q, w) for q, w in items)
    return f'<div class="marquee{" reverse" if reverse else ""}"><div class="marquee__track">{cards}{cards}</div></div>'


def hero(img, h1, p=None, short=False, light=False, pos="center 30%", cta=True):
    return f"""<section class="hero{' short' if short else ''}{' light' if light else ''}">
  <div class="hero__media"><div class="hero__reveal" style="position:absolute;inset:0"><img src="{IMG}{img}" alt="" style="object-position:{pos}" fetchpriority="high"></div></div>
  <div class="wrap">
    <h1 class="breathe-in">{h1}</h1>
    {f'<p class="rv rv-d2">{p}</p>' if p else ''}
    {f'<a class="btn light rv rv-d3" href="{WA}" target="_blank" rel="noopener">Agenda tu cita</a>' if cta else ''}
  </div>
  <div class="hero__scroll" aria-hidden="true"><span>Respira</span><i></i></div>
</section>"""


T_HOME = [
 ("“Me siento tan feliz! Liberaste a mi niña interior, volví a reír, a quererme, a valorarme y a entender que yo tengo el control de mi vida”", "Mónica"),
 ("“Andre gracias por enseñarme a fluir, a soltar todo lo que no controlo y a confiar en mí misma y en los tiempos del universo”", "Juliana"),
 ("“Esta terapia es una chimba! Demasiado poderoso entender cómo cosas de nuestro pasado marcan nuestro comportamiento y cómo nos sentimos todos los días”", "Paola"),
 ("“Fue demasiado poderoso y me dio claridad total de muchas cosas. Gracias por darme herramientas para encontrar esa paz que tanto buscamos y sobre todo por fortalecerme”", "Gabriela"),
 ("“La terapia me sirvió muchísimo para entender algunas creencias que no me estaban dejando llegar a mi máximo potencial”", "Camilo"),
 ("“Gracias por ayudarme a entender que mi problema no era lo que comía, sino todo lo que me comía a mí. Hace 3 meses tuve la sesión contigo y he logrado bajar 7 kilos”", "Alejandra"),
 ("“Me di cuenta de que nada era mi culpa, gracias por permitirme amar y confiar en que me merezco cosas maravillosas, sé que vendrán”", "Laura"),
 ("“Soy de nuevo esa niña que le decían risitas en el colegio y que se había desvanecido por los dolores de los otros”", "Camila"),
 ("“Gracias por liberarme todas mis emociones y de perdonar. Desde que nos vimos no he vuelto a tener pesadillas ni ataques de ansiedad”", "Santiago"),
]
T_RTT = [
 ("“Gracias por devolverme la confianza en mí misma, acabo de hacer una presentación y por primera vez no se me olvidó nada, mi voz estuvo calmada y pude comunicar todo lo que quería”", "Valentina"),
 ("“No sabes la tranquilidad, la paz, ¡todo lo bueno! Esta es la yo que sabía que tenía adentro pero no había podido salir”", "Lucía"),
 ("“Andre, todavía no lo puedo creer, fui capaz de montarme al avión tranquila, durante el vuelo ver una película fresca, y se me pasó literal volando. ¡Gracias infinitas!”", "Ma. Paula"),
 ("“Lo que más me gustó fue el audio personalizado que recibí. Lo escuché durante 30 días e incluso aún lo hago”", "Felipe"),
 ("“Recomiendo mucho la terapia para descubrir patrones de nuestro subconsciente que no sabemos que están ahí. Es un regalo para uno mismo”", "Sebastián"),
 ("“Nunca hubiera podido hacer la conexión de que mi problema de piel estuviera relacionado con lo que sentía acerca de mi trabajo. Una vez logré expresar mi inconformidad mi piel sanó. ¡Gracias!”", "Paciente RTT"),
 ("“El audio es muy poderoso, me ayudó a superar esas creencias que me limitaban de una forma muy contundente y rápida”", "Camilo"),
 ("“Desde que hice la terapia estoy jugando fútbol increíble, se me quitaron todas mis inseguridades y todo está saliendo de la forma que quiero”", "Jerónimo"),
 ("“Andre la terapia fue muy liberadora, y tu audio logró sanar mi cuerpo como ningún otro remedio o terapia que he hecho. Infinita gratitud”", "Andrea"),
]

# ------------------------------------------------------------------ PÁGINAS
pages = {}

pages["/"] = dict(
 title="Space to Rise · Hipnoterapia RTT en Bogotá y online | Andrea Zafra",
 desc="Sana tu cuerpo, tu mente y alcanza tus objetivos con RTT (Terapia de Transformación Rápida), coaching, baño de gong y audios de autohipnosis. Sesiones en Bogotá y online.",
 dark=True,
 body=hero("Home-Principal-New.jpg", "Sana, transfórmate y evoluciona en quien estás destinado a ser",
           "A place to heal, transform and rise to your new potential.") + f"""
<section>
  <div class="wrap split">
    <div class="split__media"><div class="frame"><img src="{IMG}3.-Home-heal-New.jpg" alt="Mujer respirando en calma"><div class="veil"></div></div></div>
    <div>
      <p class="eyebrow rv">Terapia de Transformación Rápida</p>
      <h2 class="rv">¿Qué es RTT?</h2>
      <p class="lead rv rv-d1" style="margin-top:20px">Libérate de todo lo que te está bloqueando o enfermando. Empodérate de tu propia salud reprogramando tu mente y tu corazón.</p>
      <p class="rv rv-d2">Nuestra misión es sanar, transformar y elevar la vida de millones de personas para ayudarlas a alcanzar su mejor versión. Al despertar tu mundo, iluminas el mundo.</p>
      <a class="btn rv rv-d3" href="/rtt/">Conoce más</a>
    </div>
  </div>
</section>

<section class="video-stage" aria-label="Video: Terapia RTT">
  <div class="sticky">
    <div class="frame-v">
      <video src="/assets/video/rtt.mp4" poster="/assets/video/rtt-poster.jpg" playsinline preload="metadata" loop></video>
      <button class="play" aria-label="Reproducir con sonido"><span><svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg></span></button>
    </div>
    <p class="caption">Sigue bajando: así es una terapia RTT</p>
  </div>
  <div class="spacer"></div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="center narrow" style="margin:0 auto 48px">
      <p class="eyebrow rv">Tres caminos, una misma raíz</p>
      <h2 class="rv">Heal · Rise · Shine</h2>
    </div>
    <div class="trio">
      <a class="card-img" href="/heal-rise-shine/#heal"><img src="{IMG}HEAL.jpg" alt=""><div class="card-img__body"><h3>Heal</h3><p>Sana tu cuerpo</p><span class="more"><i></i>Ver más</span></div></a>
      <a class="card-img" href="/heal-rise-shine/#rise"><img src="{IMG}Rise.jpg" alt=""><div class="card-img__body"><h3>Rise</h3><p>Sana tu mente</p><span class="more"><i></i>Ver más</span></div></a>
      <a class="card-img" href="/heal-rise-shine/#shine"><img src="{IMG}Shine.jpg" alt=""><div class="card-img__body"><h3>Shine</h3><p>Alcanza tus objetivos</p><span class="more"><i></i>Ver más</span></div></a>
    </div>
  </div>
</section>

<section class="ivory tight" style="padding-left:0;padding-right:0">
  <div class="wrap center narrow" style="margin-bottom:40px"><h2 class="rv">Lo que dicen después de una sesión</h2></div>
  {marquee(T_HOME)}
</section>

<section>
  <div class="wrap split flip">
    <div class="split__media"><div class="frame"><img src="{IMG}KIDS1Filtros.jpg" alt="Niña saltando en la playa" style="object-position:center 40%"><div class="veil"></div></div></div>
    <div>
      <p class="eyebrow rv">Kids · Niños</p>
      <h2 class="rv">RTT para niños</h2>
      <p class="quote rv rv-d1" style="font-size:clamp(1.3rem,2.2vw,1.7rem);margin:20px 0">“Lo más valioso que puedes enseñarles a tus hijos es que son suficientes”<cite>Marisa Peer</cite></p>
      <a class="btn rv rv-d2" href="/kids/">Conoce más</a>
    </div>
  </div>
</section>

<section class="sage tight">
  <div class="wrap grid grid-2">
    <a class="card-img" href="/coaching/" style="aspect-ratio:16/11"><img src="{IMG}2.-Home-Coaching-New.jpg" alt=""><div class="card-img__body"><h3>Coaching</h3><p>¡Combina lo mejor de ambos mundos!</p><span class="more"><i></i>Conoce más</span></div></a>
    <a class="card-img" href="/gong/" style="aspect-ratio:16/11"><img src="{IMG}Gong_Home.jpg" alt=""><div class="card-img__body"><h3>Gong</h3><p>Sana y transforma tu vida con la vibración divina de los sonidos del universo</p><span class="more"><i></i>Conoce más</span></div></a>
  </div>
</section>

<section>
  <div class="wrap split">
    <div class="split__media orbit rv">
      <img class="c0" src="{IMG}Circulo1-e1743521441837.png" alt="">
      <div class="ring"><img class="c1" src="{IMG}Circulo2.png" alt=""><img class="c2" src="{IMG}Circulo3.png" alt=""><img class="c3" src="{IMG}Circulo4.png" alt=""><img class="c4" src="{IMG}Circulo5.png" alt=""></div>
    </div>
    <div>
      <p class="eyebrow rv">Shop</p>
      <h2 class="rv">Conoce nuestra selección de audios</h2>
      <p class="lead rv rv-d1" style="margin-top:20px">Desbloquea tu potencial en todas las áreas de tu vida, en la salud, en el amor, en la abundancia y mucho más, con nuestra selección de audios de autohipnosis.</p>
      <a class="btn rv rv-d2" href="/shop/">Ver audios</a>
    </div>
  </div>
</section>
""")

pages["/rtt/"] = dict(
 title="¿Qué es RTT? Hipnoterapia de Transformación Rápida | Space to Rise",
 desc="RTT (Rapid Transformational Therapy) de Marisa Peer combina hipnosis, PNL y neurociencia para sanar en 1 a 3 sesiones. Conoce cómo funciona, qué puedes sanar y cómo es una sesión.",
 dark=True,
 body=hero("3.-Home-heal-New.jpg", "¿Qué es RTT: Terapia de Transformación Rápida?", None, short=True, pos="center 25%") + f"""
<section>
  <div class="wrap split">
    <div>
      <p class="lead rv">Es una terapia desarrollada por Marisa Peer (terapeuta inglesa) que combina los principios más eficaces de Hipnosis, PNL (Programación Neurolingüística) y Neurociencia para obtener resultados rápidos, permanentes y transformadores. Generalmente los pacientes logran sanar en 1 o máximo 3 sesiones dependiendo la complejidad del tema.</p>
      <p class="rv rv-d1">La hipnosis se utiliza para acceder a tu subconsciente, la parte de nuestra mente donde se encuentra toda nuestra programación y están almacenadas todas nuestras memorias y creencias, para poder entender por qué nos comportamos y reaccionamos de la forma que lo hacemos; encontrar la raíz de nuestros problemas; sanarlos y poder posteriormente crear nuevas conexiones neuronales que permiten que nos transformemos en la mejor versión de nosotros mismos.</p>
      <p class="rv rv-d2">Es una técnica espectacular que te empodera a ti en tu proceso de sanación ya que entender es poder, y una vez que entiendes la raíz y el porqué de tus problemas sanar es fácil.</p>
    </div>
    <div class="split__media"><div class="frame"><img src="{IMG}RTT-Image-2.jpg" alt="Mujer frente al mar"><div class="veil"></div></div></div>
  </div>
</section>

<section class="ivory">
  <div class="wrap split flip">
    <div class="split__media"><div class="frame square"><img src="{IMG}RTT-Image-1.jpg" alt="Mariposa"><div class="veil"></div></div></div>
    <div>
      <h2 class="rv">¿Por qué la Terapia de Transformación Rápida es tan efectiva?</h2>
      <p class="rv rv-d1" style="margin-top:20px">RTT te permite cambiar tu perspectiva y cambiar tus creencias a nivel subconsciente.</p>
      <p class="rv rv-d2">Todos estamos acostumbrados a funcionar con la mente consciente (la parte lógica y racional); sin embargo, esta es cancelada constantemente por los pensamientos y creencias de la mente subconsciente que manejan el 95% de nuestras decisiones. Por eso, aunque queramos cambiar de una forma consciente, usando la lógica y fuerza de voluntad, hasta que no logremos cambiar nuestro subconsciente ningún cambio será real y permanente.</p>
      <p class="rv rv-d3">El objetivo de RTT es liberarte de creencias limitantes y «programas» obsoletos que pueden ser la causa de tu enfermedad o bloqueos en tu vida, y “recablear” los canales neuronales de tu mente, «recodificar» tu “sistema operativo” con nuevas creencias positivas que se volverán los nuevos «programas» que transformarán tu vida.</p>
    </div>
  </div>
</section>

<section class="video-stage" aria-label="Video: Terapia RTT">
  <div class="sticky">
    <div class="frame-v">
      <video src="/assets/video/rtt.mp4" poster="/assets/video/rtt-poster.jpg" playsinline preload="metadata" loop></video>
      <button class="play" aria-label="Reproducir con sonido"><span><svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg></span></button>
    </div>
    <p class="caption">Sigue bajando para ver cómo es una terapia</p>
  </div>
  <div class="spacer"></div>
</section>

<section>
  <div class="wrap">
    <div class="narrow" style="margin-bottom:40px"><h2 class="rv">¿Qué puedo sanar con RTT?</h2><p class="rv rv-d1" style="margin-top:14px">Con RTT puedes sanar muchísimos temas. Es una terapia apta para niños y adultos.</p></div>
    <div class="grid grid-3">
      <div class="rv"><h4 class="serif" style="font-size:1.5rem;margin-bottom:12px">Enfermedades físicas</h4><p>Enfermedades genéticas, crónicas y autoinmunes; problemas de piel, pelo y digestivos, alergias, asma, dolores crónicos.</p></div>
      <div class="rv rv-d1"><h4 class="serif" style="font-size:1.5rem;margin-bottom:12px">Temas emocionales</h4><p>Ansiedad, estrés, problemas de autoestima y sentimientos de insuficiencia, fobias y miedos, adicciones, insomnio y trastornos de sueño, control de peso y trastornos alimenticios, temas de fertilidad y relaciones personales.</p></div>
      <div class="rv rv-d2"><h4 class="serif" style="font-size:1.5rem;margin-bottom:12px">Temas de desempeño</h4><p>Alcanzar metas y objetivos, mejorar tu rendimiento deportivo y empresarial.</p></div>
    </div>
  </div>
</section>

<section class="sand">
  <div class="wrap">
    <div class="narrow" style="margin-bottom:24px"><h2 class="rv">¿Cómo son las sesiones de RTT?</h2><p class="rv rv-d1" style="margin-top:14px">Una sesión de RTT se divide en 3 partes:</p></div>
    <div class="step rv"><div class="n">1</div><div><h4>Llamada inicial de 20/30 minutos</h4><p>Se utiliza para clarificar cualquier duda acerca de la terapia.</p></div></div>
    <div class="step rv"><div class="n">2</div><div><h4>La terapia</h4><p>Dura aproximadamente 2 horas. A través de la hipnosis, se realiza una regresión a tu pasado para encontrar la raíz de tu problema, entender por qué y cuándo lo creaste, y liberarte de este al cambiar viejas creencias por nuevas, para tu transformación.</p></div></div>
    <div class="step rv"><div class="n">3</div><div><h4>Audio personalizado</h4><p>Después de la sesión, te hago un audio personalizado de 15-20 minutos, que deberás escuchar todos los días por mínimo 21 días. Este es el tiempo que la mente necesita para formar nuevas conexiones neuronales y crear nuevos hábitos. La mente aprende por repetición, por lo que es fundamental escucharlo diariamente para evitar recaer en los mismos comportamientos y asegurar que el cambio sea permanente.</p></div></div>
    <div style="margin-top:36px"><a class="btn rv" href="{WA}" target="_blank" rel="noopener">Agenda tu cita</a></div>
  </div>
</section>

<section>
  <div class="wrap grid grid-2">
    <div>
      <h3 class="rv">¿Por qué RTT sana en una sola sesión?</h3>
      <p class="rv rv-d1" style="margin-top:16px">La hipnosis es el método más efectivo de identificar el origen de las creencias que te bloquean. Cuando eres capaz de observar cómo adquiriste las creencias que hoy en día te bloquean o no te sirven, es relativamente fácil dejarlas ir y crear nuevas creencias que te ayuden a avanzar. Los eventos traumáticos del pasado no son revividos, simplemente observados desde una perspectiva diferente de la persona adulta que eres hoy.</p>
    </div>
    <div>
      <h3 class="rv">¿Cómo se siente estar hipnotizado?</h3>
      <p class="rv rv-d1" style="margin-top:16px">La mayoría de las personas se sienten súper relajadas. Todo el tiempo estás 100% en control de tu cuerpo: si quieres hablar, sentarte, coger un kleenex, acomodarte, lo puedes hacer sin problema. Es un estado de relajación profundo donde tu sistema nervioso y tu mente consciente duermen, pero activas tu mente subconsciente. Tienes siempre el control de aceptar solo las sugerencias que tú quieras. Nunca podré hacerte hacer algo que no quieras.</p>
    </div>
  </div>
</section>

<section class="ivory">
  <div class="wrap">
    <h2 class="rv narrow">¿Cómo se ven los resultados?</h2>
    <p class="rv rv-d1" style="margin:14px 0 36px">3 formas en las que puedes ver los resultados:</p>
    <div class="grid grid-3">
      <div class="rv"><h4 class="serif" style="font-size:1.6rem;margin-bottom:10px">Inmediatos</h4><p>Hay clientes que salen de mi consultorio sintiéndose nuevos, livianos, aliviados de por fin haber entendido el origen y la causa de sus comportamientos, y nunca más vuelven a interpretar el mundo desde la visión que causó el problema.</p></div>
      <div class="rv rv-d1"><h4 class="serif" style="font-size:1.6rem;margin-bottom:10px">Progresivos</h4><p>Podrás ver los resultados en unos diez días, porque solo toma un mínimo de diez días, y un máximo de veintiún días, para dejar atrás viejas creencias y hábitos negativos y reemplazarlos con nuevas creencias positivas.</p></div>
      <div class="rv rv-d2"><h4 class="serif" style="font-size:1.6rem;margin-bottom:10px">Retroactivos</h4><p>A veces es la gente a nuestro alrededor la que percibe el cambio primero que nosotros.</p></div>
    </div>
  </div>
</section>

<section class="tight" style="padding-left:0;padding-right:0">
  <div class="wrap center narrow" style="margin-bottom:40px"><h2 class="rv">Testimonios</h2></div>
  {marquee(T_RTT, reverse=True)}
</section>
""")

def hrs_testimonios_heal():
    return marquee([
     ("“Soy de nuevo esa niña que le decían risitas en el colegio y que se había desvanecido por los dolores de los otros”","Camila"),
     ("“No sabes la tranquilidad, la paz, ¡todo lo bueno! Esta es la yo que sabía que tenía adentro pero no había podido salir”","Lucía"),
     ("“Fue demasiado poderoso y me dio claridad total de muchas cosas. Gracias por darme herramientas para encontrar esa paz que tanto buscamos y sobre todo por fortalecerme”","Gabriela"),
     ("“Gracias por liberar mi niña interior, volví a reír, a quererme, a valorarme y a entender que yo tengo el control de mi vida”","Mónica"),
     ("“André gracias por enseñarme a fluir, a soltar todo lo que no controlo y a confiar en mí misma y en los tiempos del universo”","Juliana"),
    ])

def hrs_testimonios_rise():
    return marquee([
     ("“Gracias por devolverme la confianza en mí misma, acabo de hacer una presentación y por primera vez en años no se me olvidó nada de lo que quería decir, mi voz estuvo calmada y relajada y pude comunicar todo lo que tenía que decir”","Valentina"),
     ("“Gracias por ayudarme a entender que mi problema no era lo que estaba comiendo, sino todos los sentimientos que me comían a mí. Hace tres meses tuve la sesión contigo y ya he logrado adelgazar mis primeros 7 kilos. ¡Gracias!”","Alejandra"),
     ("“André gracias por liberarme de todas mis emociones reprimidas y permitir sacarlas de mi ser y de perdonar a todos los que me hicieron daño. Desde que tuvimos la sesión no he vuelto a tener pesadillas, duermo perfecto y no he vuelto a tener ataques de ansiedad”","Santiago"),
     ("“Gracias por permitirme darme cuenta de que nada era mi culpa, gracias por permitirme amar y confiar en que me merezco cosas maravillosas en mi vida. Sé que vendrán”","Laura"),
     ("“Desde que hice la terapia estoy jugando fútbol increíble, se me quitaron todas mis inseguridades y todo está saliendo de la forma que quiero. Gracias”","Jerónimo"),
    ], reverse=True)

pages["/heal-rise-shine/"] = dict(
 title="Heal · Rise · Shine — Sana tu cuerpo, sana tu mente, alcanza tus objetivos | Space to Rise",
 desc="Hipnoterapia RTT para sanar enfermedades físicas (Heal), ansiedad, autoestima, adicciones y miedos (Rise) y para alcanzar tus objetivos en el deporte y los negocios (Shine).",
 dark=True,
 body=hero("Ansiedad-scaled.jpg", "Heal · Rise · Shine", "Sana tu cuerpo. Sana tu mente. Alcanza tus objetivos.", short=True, pos="center 20%") + f"""
<section class="tight">
  <div class="wrap trio">
    <a class="card-img" href="#heal"><img src="{IMG}HEAL.jpg" alt=""><div class="card-img__body"><h3>Heal</h3><p>Sana tu cuerpo</p><span class="more"><i></i>Ver más</span></div></a>
    <a class="card-img" href="#rise"><img src="{IMG}Rise.jpg" alt=""><div class="card-img__body"><h3>Rise</h3><p>Sana tu mente</p><span class="more"><i></i>Ver más</span></div></a>
    <a class="card-img" href="#shine"><img src="{IMG}Shine.jpg" alt=""><div class="card-img__body"><h3>Shine</h3><p>Alcanza tus objetivos</p><span class="more"><i></i>Ver más</span></div></a>
  </div>
</section>

<section id="heal" class="ivory">
  <div class="wrap">
    <div class="split">
      <div>
        <p class="eyebrow rv">Heal · Sana tu cuerpo</p>
        <p class="quote rv">“El dolor que no logra expresarse a través de lágrimas, hace que otros órganos lloren”<cite>Sir Henry Maudsley</cite></p>
        <p class="rv rv-d1" style="margin-top:28px">Cualquier emoción reprimida puede ser la causa de enfermedades físicas. Nuestra mente y nuestro cuerpo están conectados y cuando no logramos expresar nuestras emociones y son reprimidas nuestro cuerpo se apodera de ellas y las expresa en forma de enfermedad.</p>
        <p class="rv rv-d2">RTT es muy efectiva para encontrar la causa raíz de estos bloqueos y emociones porque, a través de la hipnosis, logras acceder a tu subconsciente, donde se guardan todas tus memorias y emociones y logras entender y reinterpretar lo que pasó para sanar.</p>
        <p class="rv rv-d2">Durante una sesión de RTT, puedes recordar experiencias pasadas, eventos traumáticos o patrones de pensamiento que pueden estar relacionados con tu problema de salud. Al identificar y entender estas memorias, puedes darles otra interpretación y empezar a cambiar tus creencias y comportamientos que pueden haber contribuido a tu enfermedad.</p>
        <p class="lead rv rv-d3">Tu mente puede crear cualquier enfermedad, pero al igual que la puede crear la puede eliminar.</p>
        <p class="rv rv-d3">Si tienes cualquier enfermedad física o autoinmune y quieres aliviar tus síntomas y encontrar la raíz de tu enfermedad, amaría ayudarte.</p>
      </div>
      <div class="split__media">
        <div class="frame"><img src="{IMG}Heal2.jpg" alt=""><div class="veil"></div></div>
        <div style="margin-top:32px" class="rv">
          <p class="caps" style="color:var(--taupe);margin-bottom:10px">Temas con los que he trabajado</p>
          <div class="cols"><ul class="list"><li>Cáncer</li><li>Dolores crónicos</li><li>Enfermedades genéticas</li><li>Enfermedades autoinmunes</li><li>Problemas de audición</li></ul><ul class="list"><li>Problemas de visión</li><li>Asma</li><li>Problemas de piel</li><li>Problemas de pelo</li><li>Alergias</li></ul></div>
          <div class="price">$450.000<small>COP · sesión</small></div>
          <a class="btn" href="{WA}" target="_blank" rel="noopener">Agenda tu cita</a>
        </div>
      </div>
    </div>
  </div>
</section>
<section class="ivory tight" style="padding-top:0;padding-left:0;padding-right:0">{hrs_testimonios_heal()}</section>

<section id="rise">
  <div class="wrap">
    <div class="split flip">
      <div class="split__media">
        <div class="frame"><img src="{IMG}4.Rise-en-vez-de-mano-scaled.jpg" alt=""><div class="veil"></div></div>
      </div>
      <div>
        <p class="eyebrow rv">Rise · Sana tu mente</p>
        <p class="quote rv">“Puede que no seamos responsables de cómo el mundo moldea nuestra mente, pero podemos aprender a ser responsables de la mente con la que creamos nuestro mundo”</p>
        <p class="rv rv-d1" style="margin-top:28px">El 95% de las decisiones de nuestra vida están construidas por todas las memorias que almacenamos en nuestro subconsciente o nuestro “disco duro”. Lo que vemos se encuentra determinado por las experiencias de nuestro pasado.</p>
        <p class="rv rv-d2">Para tener un cambio permanente en nuestra vida y sanar permanentemente, tenemos que encontrar la raíz de nuestro dolor y de nuestros problemas; de nada sirve tratar solo los síntomas, tener fuerza de voluntad y pensamientos positivos, porque el subconsciente y la emoción siempre le ganarán a la lógica y a la fuerza de voluntad.</p>
        <p class="rv rv-d2">RTT te permite encontrar estas memorias y reinterpretarlas desde tu mente adulta y no la de un niño, entendiendo y sanando para evolucionar y transformar.</p>
        <div class="rv rv-d3" style="margin-top:24px">
          <div class="cols"><ul class="list blush"><li>Ansiedad / Ataques de pánico</li><li>Baja autoestima / Sentirse insuficiente</li><li>Estrés</li><li>Autosabotaje</li><li>Adicciones: drogas, cigarrillo, vapeadores, alcohol, juego</li><li>Insomnio / Trastornos de sueño</li><li>Depresión</li></ul><ul class="list blush"><li>Fobias / Miedos: miedo de volar, de agujas, claustrofobia</li><li>Fertilidad: FIV / mejora la calidad de tus óvulos y/o esperma</li><li>Concentración / Procrastinación</li><li>Miedo de hablar en público</li><li>Duelos</li><li>Celos</li></ul></div>
          <div class="price">$450.000<small>COP · sesión</small></div>
          <a class="btn" href="{WA}" target="_blank" rel="noopener">Agenda tu cita</a>
        </div>
      </div>
    </div>
  </div>
</section>
<section class="tight" style="padding-top:0;padding-left:0;padding-right:0">{hrs_testimonios_rise()}</section>

<section id="shine" class="sand">
  <div class="wrap">
    <div class="split">
      <div>
        <p class="eyebrow rv">Shine · Alcanza tus objetivos</p>
        <h2 class="rv">¡Brilla, alcanza todos tus objetivos!</h2>
        <p class="quote rv rv-d1" style="font-size:clamp(1.2rem,2vw,1.6rem);margin:22px 0">«Tus palabras crean tu realidad, si no te gusta tu realidad, cambia tus palabras.»</p>
        <p class="rv rv-d2">Conviértete en tu mejor versión y alcanza todos tus sueños. Libérate de lo que te impide ser y reprograma tu mente para alcanzar todo lo que quieres.</p>
        <p class="rv rv-d2">RTT te permite encontrar la causa raíz de lo que te detiene, y el audio de transformación personal, especialmente hecho para ti, reprograma tu mente para alcanzar todos tus objetivos.</p>
        <div class="price rv rv-d3">$450.000<small>COP · sesión</small></div>
        <a class="btn rv rv-d3" href="{WA}" target="_blank" rel="noopener">Agenda tu cita</a>
      </div>
      <div class="split__media"><div class="frame"><img src="{IMG}Shine-scaled.jpg" alt=""><div class="veil"></div></div></div>
    </div>
    <div class="grid grid-2" style="margin-top:clamp(48px,7vw,96px)">
      <div class="rv">
        <h3 style="margin-bottom:18px">Para deportistas de alto rendimiento</h3>
        <ul class="list"><li><span><b style="font-weight:500">Mejora tu rendimiento deportivo.</b> Muchos deportistas de alto rendimiento utilizan técnicas de hipnosis para mejorar su rendimiento y superar obstáculos mentales. RTT te ayuda a entender qué te puede estar bloqueando o limitando para alcanzar tu máximo potencial y, mediante técnicas de visualización, te convierte en el deportista que siempre has querido ser, desafiando y alcanzando todos tus objetivos.</span></li><li><span><b style="font-weight:500">Aumenta tu confianza y reduce la ansiedad.</b> RTT también te ayuda a reforzar tu confianza, tu concentración, y a reducir la ansiedad, el estrés y el miedo al fracaso, permitiéndote competir con mayor seguridad y determinación.</span></li><li><span><b style="font-weight:500">Te acompañamos durante tu camino.</b> Te acompañamos a través de tu proceso y crecimiento, trabajando cada mes en un tema puntual que te ayude a superar cualquier obstáculo.</span></li></ul>
      </div>
      <div class="rv rv-d1">
        <h3 style="margin-bottom:18px">Para profesionales y emprendedores</h3>
        <ul class="list"><li><span><b style="font-weight:500">Capacidades profesionales y liderazgo.</b> Si eres un profesional o emprendedor que busca aumentar su capacidad de resolución, liderazgo, creatividad, confianza, autoestima y consecución de metas, o mejorar tu capacidad de hablar en público, llegaste al lugar que necesitabas.</span></li><li><span><b style="font-weight:500">Reduce el estrés y la ansiedad.</b> Te ayudamos a ti y a tus equipos a reducir el estrés y la ansiedad.</span></li><li><span><b style="font-weight:500">Elimina cualquier bloqueo.</b> Te ayudamos a eliminar la procrastinación, cualquier relación negativa con el dinero y te ayudamos a manifestar lo que realmente quieres.</span></li></ul>
      </div>
    </div>
  </div>
</section>
""")

pages["/kids/"] = dict(
 title="RTT Kids — Hipnoterapia para niños: autoestima, ansiedad y rendimiento | Space to Rise",
 desc="RTT ayuda a los niños a superar desafíos emocionales, construir una autoestima alta y manejar la ansiedad, el estrés, el bullying, las pesadillas y el rendimiento académico.",
 dark=True,
 body=hero("Nueva-Foto-Kids-scaled.jpg", "Kids · Niños", "“Lo más valioso que puedes enseñarles a tus hijos es que son suficientes” — Marisa Peer", short=True, pos="center 35%") + f"""
<section>
  <div class="wrap split">
    <div>
      <p class="lead rv">Como papás tenemos una responsabilidad gigante con nuestros hijos para ayudarlos a tener una autoestima inquebrantable para que puedan ser niños felices que se convertirán en adultos realizados y equilibrados.</p>
      <p class="rv rv-d1">Las experiencias vividas durante la infancia tienen un impacto enorme en la autoestima, las creencias, la mentalidad y la vida de una persona adulta.</p>
      <p class="rv rv-d2">La manera en que le hablamos a nuestros hijos se convierte en su voz interior y moldea su imagen propia y su percepción del mundo. Por eso es tan importante inculcar creencias positivas y construir una base sólida de autoestima, seguridad y confianza.</p>
      <p class="rv rv-d2">RTT ayuda a los niños a superar cualquier desafío emocional para que no crezcan con creencias limitantes, ayudamos a construir una autoestima alta y proporcionamos herramientas para manejar la ansiedad, el estrés y mejorar el rendimiento académico.</p>
      <div class="price rv rv-d3">$350.000<small>COP · sesión</small></div>
      <a class="btn rv rv-d3" href="{WA}" target="_blank" rel="noopener">Agenda tu cita</a>
    </div>
    <div class="split__media"><div class="frame"><img src="{IMG}Kids2.jpg" alt=""><div class="veil"></div></div></div>
  </div>
</section>
<section class="sage tight">
  <div class="wrap">
    <h2 class="rv" style="margin-bottom:28px">Temas en los que podemos ayudar</h2>
    <div class="grid grid-3">
      <ul class="list rv"><li>Tener una autoestima alta (temas de bullying)</li><li>Disminuir la ansiedad y el estrés</li></ul>
      <ul class="list rv rv-d1"><li>Mejorar rendimiento académico</li><li>Pasar exámenes</li><li>Pesadillas / Sueño</li></ul>
      <ul class="list rv rv-d2"><li>ADHD</li><li>Dislexia</li></ul>
    </div>
  </div>
</section>
<section class="tight">
  <div class="wrap"><div class="frame wide"><img src="{IMG}Imagen_Kids_Home.jpg" alt="Niños haciendo muecas" style="object-position:center 40%"><div class="veil"></div></div></div>
</section>
""")

pages["/coaching/"] = dict(
 title="Coaching individual + RTT — ¡Combina lo mejor de ambos mundos! | Space to Rise",
 desc="Sesiones de coaching individual de 1 hora por Zoom para implementar los cambios que descubriste con RTT y no volver a los patrones del pasado.",
 dark=True,
 body=hero("image.jpg", "Coaching", "¡Combina lo mejor de ambos mundos!", short=True, pos="center 40%") + f"""
<section>
  <div class="wrap split">
    <div class="split__media"><div class="frame"><img src="{IMG}Nueva-Foto-Coaching-scaled.jpg" alt=""><div class="veil"></div></div></div>
    <div>
      <p class="lead rv">Con RTT trabajamos tu mente subconsciente, entendiendo el porqué de tus comportamientos y la raíz de tus problemas, y con las sesiones de coaching individual te ayudo a implementar los cambios necesarios en tu vida para que nunca más vuelvas a usar los patrones del pasado ni a autosabotear tu transformación.</p>
      <div class="rv rv-d1" style="margin-top:28px;padding-top:24px;border-top:1px solid var(--line)">
        <p class="caps" style="color:var(--taupe);margin-bottom:6px">Coaching individual</p>
        <p style="margin:0">Sesiones de 1 hora por Zoom</p>
        <div class="price">$180.000<small>COP · sesión</small></div>
        <a class="btn" href="{WA}" target="_blank" rel="noopener">Agenda tu cita</a>
      </div>
    </div>
  </div>
</section>
""")

pages["/gong/"] = dict(
 title="Baño de Gong en Bogotá — Sana con la vibración del sonido | Space to Rise",
 desc="El baño de gong es una técnica de relajación profunda a través de la vibración de este instrumento ancestral. Sesiones individuales y grupales en Bogotá.",
 dark=True,
 body=hero("Gong_Home.jpg", "Gong", "Sana y transforma tu vida con la vibración divina de los sonidos del universo", short=True, pos="center 50%") + f"""
<section>
  <div class="wrap split">
    <div>
      <p class="lead rv">El baño de Gong es una técnica de relajación profunda que se alcanza a través de las vibraciones que produce el sonido de este instrumento ancestral.</p>
      <p class="rv rv-d1">Su sonido y vibración facilita el proceso de regeneración celular, la autocuración del cuerpo, promueve el bienestar físico, mental y emocional, equilibra los centros de energía del cuerpo (los chakras), libera el flujo de energía y cualquier emoción reprimida.</p>
      <p class="rv rv-d2">Más que un instrumento musical el Gong es un sistema intervibracional: el Gong recibe las energías de la persona, las armoniza y las transforma para retornarlas potencializadas con una intención, que es una energía muy poderosa capaz de liberar cualquier memoria reprimida o enfermedad de tu cuerpo y tener más claridad sobre lo que quieras solucionar.</p>
      <p class="rv rv-d2">Puede ser una terapia complementaria para enfermedades a nivel celular como cáncer ya que su vibración es tan poderosa y pura que hace vibrar todas las células de tu cuerpo, fomentando el proceso de regeneración celular y autocuración del cuerpo.</p>
      <p class="lead rv rv-d3">Regálate esta experiencia única y déjame acompañarte en este viaje sonoro hacia tu bienestar.</p>
    </div>
    <div class="split__media"><div class="frame"><img src="{IMG}EC5B0F01-906B-49CF-BFBC-83D8E23D25F6.jpg" alt="Baño de gong grupal"><div class="veil"></div></div></div>
  </div>
</section>
<section class="sage tight">
  <div class="wrap grid grid-2" style="align-items:center">
    <div class="rv">
      <h2>Sesiones</h2>
      <ul class="list" style="margin-top:20px"><li><span>Sesión individual <b style="font-weight:500;margin-left:8px">$150.000</b></span></li><li><span>Sesión grupal <b style="font-weight:500;margin-left:8px">$100.000</b> por persona</span></li></ul>
      <div style="margin-top:26px"><a class="btn" href="{WA}" target="_blank" rel="noopener">Agenda tu cita</a></div>
    </div>
    <div class="frame square rv"><img src="{IMG}Gong2.jpg" alt="" style="object-position:center 20%"><div class="veil"></div></div>
  </div>
</section>
""")

SHOP_CATS = [("Circulo1-e1743521441837.png", "Trabaja en ti, sana tu cuerpo y mente"), ("Circulo2.png", "Libérate de todo lo que no quieres"), ("Circulo3.png", "Supera todos tus miedos"), ("Circulo4.png", "Desarrollo profesional"), ("Circulo5.png", "Proyectos de vida")]
pages["/shop/"] = dict(
 title="Audios de autohipnosis — Shop | Space to Rise",
 desc="Audios de autohipnosis para bajar de peso, dormir, superar la ansiedad, el miedo a volar, hablar en público, atraer abundancia y más. Reconfigura tu mente en menos de 20 minutos al día.",
 dark=False,
 body=hero("Shop-Principal.jpg", "Aprende a reconfigurar tu mente y cambiar tu vida en menos de 20 minutos al día", None, short=True, light=True, pos="center 30%", cta=False) + f"""
<section class="tight">
  <div class="wrap split">
    <div>
      <p class="lead rv">Desbloquea tu potencial en todas las áreas de tu vida, en la salud, en el amor, en la abundancia y mucho más con nuestra selección de audios de autohipnosis.</p>
      <p class="rv rv-d1">Con estos audios puedes crear cambios permanentes en tu vida desde donde estés. Simplemente tienes que tener un espacio donde te puedas relajar y desconectar por 15-20 minutos. Es igual que oír una meditación guiada, a diferencia de que los primeros 3 minutos te guío para que entres en un estado de hipnosis, que es una técnica muy poderosa para superar bloqueos emocionales y problemas físicos porque, a diferencia de otras formas de terapia, la hipnosis accede a tu mente subconsciente donde se almacenan nuestras creencias y emociones.</p>
      <p class="rv rv-d2">Al acceder a tu subconsciente, a través de los audios eres capaz de reprogramar patrones de pensamiento negativos/destructivos por creencias positivas y empoderadoras, transformando tu vida.</p>
      <p class="rv rv-d2">Estos audios los debes oír por un mínimo de 21 días, que es lo que se tarda tu mente en crear nuevos canales neuronales en tu cerebro, nuevos patrones y nuevos hábitos.</p>
      <p class="rv rv-d3">La hipnosis es 100% segura y puedes entrar y salir de ella muy fácilmente. Estás consciente en todo momento, solo que tu mente está mucho más receptiva y sugestionable a recibir todas las sugerencias que son buenas para ti.</p>
      <p class="lead rv rv-d3">¡Simplemente ponte tus audífonos, recuéstate y nosotros nos encargamos del resto!</p>
    </div>
    <div class="split__media orbit rv">
      <img class="c0" src="{IMG}Circulo1-e1743521441837.png" alt="">
      <div class="ring"><img class="c1" src="{IMG}Circulo2.png" alt=""><img class="c2" src="{IMG}Circulo3.png" alt=""><img class="c3" src="{IMG}Circulo4.png" alt=""><img class="c4" src="{IMG}Circulo5.png" alt=""></div>
    </div>
  </div>
</section>
<section class="ivory" style="padding-top:clamp(40px,6vw,72px)">
  <div class="wrap">
    <div class="narrow"><h2 class="rv">Elige tu audio</h2><p class="rv rv-d1" style="margin-top:12px">Después del pago recibes el audio en tu correo con las instrucciones para escucharlo durante 21 días.</p></div>
    <div data-shop></div>
  </div>
</section>
""")

pages["/acerca-de-mi/"] = dict(
 title="Acerca de mí — Andrea Zafra, terapeuta RTT | Space to Rise",
 desc="Andrea Zafra: administradora de empresas, MBA, mamá de tres y terapeuta certificada en Rapid Transformational Therapy. Su historia y su misión.",
 dark=False,
 body=f"""
<section style="padding-top:calc(clamp(72px,10vw,140px) + 60px)">
  <div class="wrap split">
    <div class="split__media about-img"><div class="frame"><img src="{IMG}AdreaZafra.jpg" alt="Andrea Zafra"><div class="veil"></div></div></div>
    <div>
      <p class="eyebrow rv">Acerca de mí</p>
      <h1 class="rv" style="font-size:clamp(2.2rem,5vw,4rem)">Andrea Zafra</h1>
      <p class="lead rv rv-d1" style="margin-top:22px">Dicen que tus hijos son tus grandes maestros y en mi caso lo son. Han despertado en mí una búsqueda constante y una curiosidad insaciable de cómo transformarme en la mejor persona que puedo ser para poderles brindar a ellos el mejor nido y poder ser una luz brillante siempre para iluminar el camino que decidan recorrer.</p>
      <p class="rv rv-d2">Así comenzó mi viaje de descubrimiento, sanación y transformación. Crecí en una familia que me dio muchísimo amor; siguiendo el ejemplo de mi papá, estudié administración de empresas seguido de un MBA en una de las mejores universidades del mundo.</p>
      <p class="rv rv-d2">Me casé con un hombre maravilloso que admiro profundamente y me siento agradecida de tenerlo a mi lado. Empecé mi vida laboral en grandes multinacionales y fundé varios negocios. Mientras, fueron naciendo mis hijos, Jerónimo, Olivia y fue hasta la llegada de Alexa que mi mundo dio un giro, un giro que me reconectó con mi verdadera esencia.</p>
    </div>
  </div>
</section>
<section class="ivory">
  <div class="wrap split flip">
    <div class="split__media"><div class="frame"><img src="{IMG}Andrea-Zafra-Coach-scaled.jpeg" alt="Andrea Zafra" style="object-position:center 20%"><div class="veil"></div></div></div>
    <div>
      <p class="rv">Paré de trabajar en el mundo corporativo y me dediqué a aprender, aprender todo lo que pudiera para crear un nido donde mis hijos pudieran crecer libres de miedos, de limitaciones, con una autoestima fuerte, con creencias expansivas, con una nutrición sana y sobre todo ofrecerles un espacio para que pudieran crecer felices. Hice muchos cursos de crianza consciente, nutrición, energía, mindfulness, yoga y todos me ayudaban a construir ese espacio, pero en el camino me di cuenta de que para realmente poderles ofrecer a ellos todo lo que yo quería primero tenía que transformarme yo misma y convertirme en ese ejemplo de persona que quería para ellos. Tenía que superar mis propios miedos, mis inseguridades, cuestionar mis creencias, sanar mi cuerpo y convertirme en una mujer expansiva, inclusiva y segura.</p>
      <p class="rv rv-d1">No podemos ofrecer al mundo algo que no somos. Así fue como decidí estudiar Rapid Transformational Therapy (RTT), transformar mi vida y la de muchas personas con las que he tenido el placer de conectar.</p>
      <p class="quote rv rv-d2" style="font-size:clamp(1.3rem,2.4vw,1.9rem);margin-top:28px">Mi misión es sanar, liberar y transformar para poder vivir desde el amor, la felicidad y la gratitud.</p>
      <div class="rv rv-d3" style="margin-top:26px"><span class="pill">RTT · Marisa Peer</span><span class="pill">Coaching</span><span class="pill">Baño de gong</span><span class="pill">MBA</span></div>
    </div>
  </div>
</section>
""")

pages["/gif-for-you/"] = dict(
 title="Gift for you — Recursos gratuitos | Space to Rise",
 desc="Audios y PDFs gratuitos para inspirarte y acompañarte: descarga los tips para reducir la ansiedad y la depresión.",
 dark=True,
 body=hero("Ansiedad-y-Depresion.jpg", "Gifts for you", "Recursos exclusivos, solo para ti.", short=True, pos="center 30%", cta=False) + f"""
<section>
  <div class="wrap split">
    <div>
      <p class="lead rv">Descubre nuestra colección de audios y PDFs gratuitos, pensados para inspirarte, impulsarte y acompañarte en cada paso. Aquí, lo mejor no tiene precio: tienes todo a tu alcance para que sigas creciendo. Explora, descarga y disfruta de contenido creado para ayudarte a crecer y aprovechar al máximo tu potencial.</p>
      <p class="rv rv-d1">Porque en Space to Rise creemos que el conocimiento debe estar al alcance de todos. ¡Empieza hoy mismo y lleva tu experiencia al siguiente nivel!</p>
    </div>
    <div class="split__media rv rv-d1">
      <div class="frame wide"><img src="{IMG}Ansiedad-y-Depresion.jpg" alt=""><div class="veil"></div></div>
      <div style="margin-top:22px">
        <h3>Tips para reducir la ansiedad y la depresión</h3>
        <p class="muted" style="margin:8px 0 18px">Guía en PDF con herramientas efectivas que puedes aplicar en tu día a día para gestionar el estrés y recuperar tu bienestar emocional.</p>
        <a class="btn" href="/assets/doc/Depresion-y-Ansiedad.pdf" download>Descarga aquí</a>
      </div>
    </div>
  </div>
</section>
""")

FAQ = [
 ("¿Qué es RTT?", "<p>Rapid Transformational Therapy / Terapia de Transformación Rápida. Es una terapia desarrollada por Marisa Peer (terapeuta inglesa) que combina los principios más eficaces de Hipnosis, PNL (Programación Neurolingüística) y Neurociencia para obtener resultados rápidos, permanentes y transformadores. Generalmente los pacientes logran sanar en 1 o máximo 3 sesiones dependiendo la complejidad del tema. El objetivo de RTT es liberarte de creencias limitantes y «programas» obsoletos que pueden ser la causa de tu enfermedad o bloqueos en tu vida, y “recablear” los canales neuronales de tu mente, «recodificar» tu “sistema operativo” con nuevas creencias positivas que se volverán los nuevos «programas» que transformarán tu vida.</p>"),
 ("¿Por qué hipnosis?", "<p>La hipnosis se utiliza para acceder a tu subconsciente, la parte de nuestra mente donde se encuentra toda nuestra programación y están almacenadas todas nuestras memorias y creencias, para poder entender por qué nos comportamos y reaccionamos de la forma que lo hacemos; encontrar la raíz de nuestros problemas; sanarlos y poder posteriormente crear nuevas conexiones neuronales que te permiten transformarte en la mejor versión de ti misma.</p>"),
 ("¿Por qué RTT es tan efectiva?", "<p>RTT te permite cambiar tu perspectiva y cambiar tus creencias a nivel subconsciente. Todos estamos acostumbrados a funcionar con la mente consciente (la parte lógica y racional), sin embargo esta es cancelada constantemente por los pensamientos y creencias de la mente subconsciente que manejan el 95% de nuestras decisiones. Por eso, aunque queramos cambiar de una forma consciente, usando la lógica y fuerza de voluntad, hasta que no logremos cambiar nuestro subconsciente ningún cambio será real y permanente.</p>"),
 ("¿Qué puedo sanar y transformar con RTT?", "<p><b style='font-weight:500'>Enfermedades físicas:</b> cáncer, enfermedades crónicas, problemas de piel, pelo y digestivos.</p><p><b style='font-weight:500'>Temas emocionales:</b> ansiedad, estrés, autoestima y sentimientos de insuficiencia, fobias, miedos y adicciones, insomnio y trastornos de sueño, control de peso y trastornos alimenticios, fertilidad, relaciones.</p><p><b style='font-weight:500'>Temas de desempeño:</b> alcanzar sueños, metas y objetivos; mejorar tu rendimiento deportivo.</p><p>* Es una terapia apta para niños y adultos.</p>"),
 ("¿Cómo son las sesiones de RTT?", "<p>Una sesión de RTT se divide en 3 partes:</p><ul><li>Una llamada de 20 minutos para clarificar cualquier duda acerca de la terapia.</li><li>La terapia per se dura aproximadamente 1:30-2 horas, donde a través de la hipnosis hacemos una regresión a tu subconsciente para encontrar la raíz de tu problema, entender por qué y cuándo lo creaste y poder liberarte de este sustituyendo viejas creencias con nuevas creencias para tu transformación.</li><li>Te haré un audio personalizado especialmente para ti de 15-20 min que oirás todos los días por un mínimo de 21 días, que es el tiempo que se tarda la mente en formar nuevas conexiones neuronales y crear nuevos hábitos en tu vida. La mente aprende por medio de la repetición; por esto es tan importante oírlo todos los días para no volver a caer en los mismos comportamientos de siempre y que el cambio sea realmente permanente.</li></ul>"),
 ("¿Por qué RTT sana en una sola sesión?", "<p>La hipnosis es el método más efectivo de identificar el origen de las creencias que te bloquean. Cuando eres capaz de observar cómo adquiriste las creencias que hoy en día te bloquean o no te sirven, es relativamente fácil dejarlas ir y crear nuevas creencias que te ayuden a avanzar. Los eventos traumáticos del pasado no son revividos, simplemente observados desde una perspectiva diferente de la persona adulta que eres hoy.</p>"),
 ("¿Cómo se siente estar hipnotizado?", "<p>La mayoría de las personas se sienten súper relajadas. Todo el tiempo estás 100% en control de tu cuerpo: si quieres hablar, sentarte, coger un kleenex, acomodarte, lo puedes hacer sin problema. Es un estado de relajación profundo donde tu sistema nervioso y tu mente consciente duermen, pero activas tu mente subconsciente. Tienes siempre el control de aceptar solo las sugerencias que tú quieras. Nunca podré hacerte hacer algo que no quieras.</p>"),
 ("¿Cómo se ven los resultados?", "<p>Hay tres formas en las que puedes ver los cambios:</p><ul><li><b style='font-weight:500'>Inmediatos:</b> hay clientes que salen de mi consultorio sintiéndose nuevos, livianos, aliviados de por fin haber entendido el origen y la causa de sus comportamientos y nunca más vuelven a interpretar el mundo desde la visión que causó el problema.</li><li><b style='font-weight:500'>Progresivos:</b> podrás ver los resultados en unos diez días, porque solo toma un mínimo de diez días, y un máximo de veintiún días, para dejar atrás viejas creencias y hábitos negativos y reemplazarlos con nuevas creencias positivas.</li><li><b style='font-weight:500'>Retroactivos:</b> a veces es la gente a nuestro alrededor la que percibe el cambio primero que nosotros.</li></ul>"),
 ("¿Cuánto tiempo dura la sesión?", "<p>Cada sesión de RTT suele durar entre 90 minutos y 2 horas. Se recomienda reservar 2 horas en tu calendario para asegurarte de tener tiempo suficiente y no estar apurado.</p>"),
 ("¿Puedes quedarte atrapado en la hipnosis?", "<p>No, tienes control completo durante toda la sesión. Puedes hablar, mover tu cuerpo, levantarte o incluso irte si es necesario. Si haces tu sesión por Zoom y la llamada se desconecta, es posible que te quedes dormido debido a la relajación, pero eventualmente te darás cuenta y abrirás los ojos.</p>"),
 ("¿Cómo funciona?", "<p>La hipnosis no es magia, se basa en principios científicos. Cuando tus ojos miran hacia arriba y comienzas a sentir un fuerte parpadeo en tus ojos, estás produciendo ondas Alpha; estas ondas cerebrales son similares a las que produce tu cerebro cuando estás soñando (REM), y gracias a ellas, el cerebro nos permite acceder a la mente subconsciente. Es simple y posible para todo el mundo.</p>"),
 ("¿Qué sucede si ves escenas dolorosas o muy duras emocionalmente?", "<p>Si vuelves a escenas relacionadas con trauma o abuso, es importante recordar que no las estás reviviendo, sino observándolas desde un entorno seguro. Estaré todo el tiempo al lado tuyo brindándote apoyo y crearé un espacio seguro para que expreses emociones y sanes.</p>"),
 ("¿Qué pasa si no vas suficientemente profundo?", "<p>La profundidad del trance no es crucial para los resultados. En lugar de centrarte en la profundidad, asegúrate a ti mismo de que «esto está funcionando», ya que la efectividad no está vinculada a la profundidad del trance.</p>"),
 ("¿Qué sucede si ya conoces el motivo de tu problema?", "<p>RTT a menudo revela una nueva perspectiva sobre problemas conocidos, lo que te permite cambiar su significado y creencias. Es posible que descubras escenas diferentes de lo que esperabas, así que relájate y confía en tu subconsciente para que te muestre lo necesario.</p>"),
 ("¿Qué sucede si necesitas o quieres otra sesión?", "<p>Si bien el objetivo de RTT es lograr avances poderosos y rápidos, algunos problemas pueden requerir múltiples sesiones, hasta tres en casos más profundos. Muchos clientes continúan con sesiones para abordar diferentes áreas de la vida o recibir coaching para integrar nuevas creencias y hábitos.</p>"),
]
faq_html = ''.join(f'<div class="acc__item"><button class="acc__q" aria-expanded="false">{q}<i></i></button><div class="acc__a"><div><div class="inner">{a}</div></div></div></div>' for q, a in FAQ)
faq_ld = json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":html.unescape(__import__('re').sub('<[^>]+>',' ',a)).strip()}} for q,a in FAQ]}, ensure_ascii=False)
pages["/preguntas-frecuentes/"] = dict(
 title="Preguntas frecuentes sobre RTT e hipnosis | Space to Rise",
 desc="¿La hipnosis es real? ¿Es segura? ¿Cuánto dura una sesión de RTT? ¿Puedo quedarme atrapado? Respuestas a las dudas más comunes sobre la Terapia de Transformación Rápida.",
 dark=False,
 body=f"""
<section style="padding-top:calc(clamp(72px,10vw,140px) + 60px)">
  <div class="wrap">
    <div class="narrow" style="margin-bottom:40px"><p class="eyebrow rv">Todo lo que quieres saber</p><h1 class="rv" style="font-size:clamp(2.2rem,5vw,4rem)">Preguntas frecuentes</h1></div>
    <div class="acc rv">{faq_html}</div>
    <div style="margin-top:40px" class="rv"><p class="muted">¿Tienes otra pregunta?</p><a class="btn" href="{WA}" target="_blank" rel="noopener">Escríbeme por WhatsApp</a></div>
  </div>
</section>
<script type="application/ld+json">{faq_ld}</script>
""")

pages["/mision/"] = dict(
 title="Misión — Sanar y transformar la vida de millones de personas | Space to Rise",
 desc="Nuestra misión es sanar y transformar la vida de millones de personas liberándolas de creencias limitantes, y ayudar a padres a criar generaciones libres de miedos.",
 dark=True,
 body=hero("Mision1.jpg", "Misión", None, short=True, pos="center 30%", cta=False) + f"""
<section>
  <div class="wrap narrow">
    <p class="quote rv">Nuestra misión es sanar y transformar la vida de millones de personas liberándolas de creencias limitantes y programas desactualizados que enferman, bloquean e impiden ser la mejor versión de nosotros mismos.</p>
    <p class="rv rv-d1" style="margin-top:28px">Trabajamos con técnicas innovadoras que nos permiten, a través de nuestro subconsciente, cambiar el comportamiento de nuestras células transformando nuestra salud y nuestra vida.</p>
    <p class="rv rv-d2">También ayudamos a padres a criar nuevas generaciones libres de miedos y creencias limitantes para que los niños logren crecer con una autoestima alta, mucho amor propio y alas fuertes y resilientes que les permitan volar alto.</p>
    <p class="quote rv rv-d3" style="font-size:clamp(1.3rem,2.4vw,1.9rem);margin-top:32px">¡Al despertar tu mundo, iluminas el mundo!<br>¡Evoluciona hacia quien estás destinado a ser!</p>
  </div>
</section>
""")

# ------------------------------------------------------------------ BUILD
for path, p in pages.items():
    d = os.path.join(OUT, path.strip('/')) if path != '/' else OUT
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(head(p['title'], p['desc'], path, p.get('dark', False)) + p['body'] + foot())
    print('wrote', path)

# sitemap + robots
sm = '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join(f'<url><loc>https://spacetorise.com{p}</loc></url>' for p in pages) + '</urlset>'
open(os.path.join(OUT, 'sitemap.xml'), 'w').write(sm)
open(os.path.join(OUT, 'robots.txt'), 'w').write('User-agent: *\nAllow: /\nSitemap: https://spacetorise.com/sitemap.xml\n')
json.dump({"cleanUrls": True, "trailingSlash": True, "redirects": [{"source": "/gift-for-you", "destination": "/gif-for-you/", "permanent": True}, {"source": "/home", "destination": "/", "permanent": True}, {"source": "/tienda", "destination": "/shop/", "permanent": True}], "headers": [{"source": "/assets/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]}]}, open(os.path.join(OUT, 'vercel.json'), 'w'), indent=1)
