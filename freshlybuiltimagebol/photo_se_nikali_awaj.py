from .photo_se_text import PhotoShabd
from .text_bol_uthega import ShabdDhwani


class PhotoAwaj:
    def photo_se_awaj(photo_ka_naam, bhasha, awaj_ka_naam):
        return ShabdDhwani.shabd_se_dhwani(
            PhotoShabd.photo_ka_text(photo_ka_naam), bhasha, awaj_ka_naam
        )

    def photo_se_bhasha_badlo(photo_ka_naam, bhasha):
        return ShabdDhwani.shabd_ki_bhasha_badlo(
            PhotoShabd.photo_ka_text(photo_ka_naam), bhasha
        )

    def photo_m_kaun_sii_bhasha(photo_ka_naam):
        return ShabdDhwani.shabd_ki_bhasha_jaano(
            PhotoShabd.photo_ka_text(photo_ka_naam)
        )


# PhotoAwaj.photo_se_awaj('test.png','hi','fg.mp3')
