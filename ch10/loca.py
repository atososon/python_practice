import locale
from datetime import date
halloween = date(2014,10,31)
for lang_country in ['en-US','fr-FR','de-DE', 'es-ES','is-IS',]:
    locale.setlocale(locale.LC_TIME, lang_country)
    print(halloween.strftime('%A, %B %d'))