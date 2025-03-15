from typing import Any
from blog.models import Post, Category
from django.core.management.base import BaseCommand
import random

class Command(BaseCommand):
    help = "This commands inserts post data"

    def handle(self, *args: Any, **options: Any):
        # Delete existing data 
        Post.objects.all().delete()

        titles = [
            'Taj Mahal',
            'Red fort',
            'Golden temple Amritsar',             
            'Amer fort',
            'Hawa mahal ',
            'Humayun tomb',
            'Qutab minar',
            'Mysore palace',
            'India fort',
            'Aguada fort',
            'Mehrangarh fort',
            'Meenakshi temple',
            'Statue of unity',
            'Kamakhya devi temple',
            'Trimbakeshwar temple',
            'Shri mahakaleshwar temple',
            'Promenade beach',
            'Prem mandir',
            'Dal lake Srinagar',
            'Akshardham temple',
        ]

        contents = [
            "Taj Mahal, located in Agra in the state of Uttar Pradesh, is widely considered as a symbol of eternal love. It is a monument built in the 17th Century. It was built during the Mughal rule, and can be summed up as a brilliant representation of grandeur that Mughal architecture stood for.",
            "A significant landmark in Delhi, the Red Fort or Lal Qila is a splendid monument from the Mughal period. It serves as a testament to the country rich cultural heritage and architectural finesse. The striking red sandstone walls coupled with delicate carvings make for a breathtaking sight.",
            "Guru Ram Das, who happened to be the fourth Sikh Guru initiated this Gurudwaras construction during the 16th century with Hazrat Mian Mir a respected Muslim saint  laying down its foundation stone as a symbol of inclusivity and unityGuru Arjan Dev who followed through to completion at 1604 A.D",
            "The magnificent Amber Fort, also called Amer Fort, graces the landscape of Jaipur, a prestigious city in Rajasthan, perched atop a hill with stunning views overlooking Maota Lake, showcasing the grandeur of the Rajput era.",
            "An iconic landmark of the city, the honeycomb-shaped palace features beautiful jharokhas and windows. This five-storey building has been built without a foundation and is known for its exceptional ventilation, which is also the reason behind its name, Hawa Mahal",
            "The royal mausoleum of Mughal Emperor Humayun, this structure was sanctioned by his widow Hamida Baga Begum and designed by Persian architect Mirak Mirza Ghiyas. It was completed between 1565 and 1572.",
            "Towering 73 metres high above the greens in Mehrauli, construction for this five-storey minaret was started by Qutb ud Din Aibak, founder of Delhi Sultanate. It is renowned for the artistic brick-work on its pillars and arches.",
            "Mysore Palace or better known as Amba Vilas Palace is an impressive historic palace located in Karnatakas city, Mysore. It is a top-rated tourist destination in India due to its remarkable architecture that has attracted millions annually throughout the country's history till now. The mighty structure plays homage to the opulent Wadiyar dynastys rich cultural heritage and architectural excellence which once ruled over the Kingdom of Mysore years ago.",
            "India Gate is an awe-inspiring monument built as a war memorial honouring Indian soldiers who demonstrated remarkable courage while serving under the British Empire during World War I and Afghan Wars. Designed by renowned British architect, Edwin Lutyens, with its foundation stone being laid down in 1921 before being completed ten years later in 1931.",
            "The illustrious Aguada Fort located in Goa, has both historic and architectural significance. Built by the Portuguese over three centuries ago around the early 17th century, this imposing fortress served as an essential defence mechanism against potential enemy invasions aimed at protecting Portuguese territories in Goa.",
            "The legacy behind Mehrangarh Fort in Jodhpurroots in its awe-inspiring architecture which portrays both valiance and grandiosity belonging to the Rathore family dynasty. This fort sits on a hill that has an elevation of up to 125 metres, boasting panoramic scenes ranging from blue city sights to surrounding zones and earning tags such as Citadel of The Sun among others.",
            "An iconic representation of South Indian architectural brilliance and spiritual devotion is embodied by the remarkable Meenakshi Temple. Located in Madurai, this ancient shrine stands unparalleled in its reverence for Goddess Meenakshi regarded as an embodiment of Parvati among devotees.It showcases the Dravidian style of architecture with its towering gopurams (entrance towers) intricately carved pillars, mandapams (halls), and ornate sculptures.",
            "Standing tall above everything else, the iconic monument known as the Statue of Unity, located in Gujarat State near city, has reached great heights, towering at an impressive altitude measuring up to 182 m",
            "The joy of travel comes in exploring new things. Planting your feet somewhere youve never been before brings with it the rush of discovery and the joy of pushing back on the boundaries of your world.",
            "Trimbakeshwar Temple is a revered Hindu shrine located in the town of Trimbak near Igatpuri in the Nashik district of Maharashtra, India. It holds great religious significance as one of the twelve Jyotirlingas, which are considered to be the most sacred abodes of Lord Shiva. The temple is beautifully nestled amidst the picturesque Sahyadri Mountains and surrounded by lush greenery, creating a serene and tranquil atmosphere.",
            "The Mahakaleshwar Temple in Ujjain boasts great esteem for serving both a historical significance as well as a spiritual purpose within India. For centuries devotees have journeyed here to offer prayers to Lord Shiva, specifically at this temple which holds distinction among other shrines due to it being one of twelve Jyotirlingas designated by Hindu tradition as some of the most sacred abodes for honoring their Gods.",
            "The beach exudes natural beauty and serene waterscapes flanked by sandy shores make for gorgeous views of the Bay of Bengal. Visitors can unwind here by taking peaceful walks or watching breathtaking sunrises and sunsets, the perfect place to recharge your batteries not just that it is home to several shops, cafes and restaurants lining its promenade. From dawn until dusk, there is always something happening around this beach.",
            "Prem Mandir, located in Mathura, is a magnificent temple complex that attracts devotees and tourists alike. The temple is dedicated to Lord Krishna and his eternal love for Radha. Built with immaculate architecture and intricate craftsmanship, Prem Mandir stands as a symbol of devotion and spirituality.The architecture of Prem Mandir is awe-inspiring. The entire complex is constructed using pristine white marble, which imparts a divine aura to the temple.",
            "Dal Lake is an enchanting destination that encapsulates the essence of Srinagar's natural beauty, cultural heritage, and vibrant traditions. Dal Lake, which covers an area of roughly 26 sq km, is frequently referred to as Srinagar's jewel. For tourists looking for a distinctive and memorable experience in Kashmir'sparadise, it is a must-visit attraction because of its calm waterways, magnificent surroundings, houseboats, floating marketplaces, and picturesque vistas.",
            "Akshardham Temple is a magnificent and awe-inspiring architectural masterpiece. Constructed in 2005, the temple stands as a tribute to Lord Swaminarayan and reflects the deep richness and spiritual depth of Indian cultural heritage. Covering ample space with intricate carvings, splendid sculptures, and breathtaking architecture, admiration fills visitors hearts.",
        ]

        img_urls = [
            
            "https://hblimg.mmtcdn.com/content/hubble/img/agra/mmt/activities/m_activities-agra-taj-mahal_l_400_640.jpg",
            "https://hblimg.mmtcdn.com/content/hubble/img/delhi/mmt/activities/m_activities_delhi_red_fort_l_341_817.jpg",
            "https://hblimg.mmtcdn.com/content/hubble/img/amritsar/mmt/activities/m_Golden%20Temple_2_l_472_709.jpg",
            "https://hblimg.mmtcdn.com/content/hubble/img/jaipur/mmt/activities/m_activities_amber_fort_2_l_436_573.jpg",
            "https://hblimg.mmtcdn.com/content/hubble/img/jaipur/mmt/activities/m_activities_hawa_mahal_1_l_258_789.jpg",
            "https://hblimg.mmtcdn.com/content/hubble/img/delhi/mmt/activities/m_activities_delhi_humayun_s_tomb_l_435_653.jpg",
            "https://hblimg.mmtcdn.com/content/hubble/img/delhi/mmt/activities/m_activities_delhi_qutab_minar_l_384_574.jpg",
            "https://hblimg.mmtcdn.com/content/hubble/img/mysore/mmt/activities/m_activities_Mysore_Mysore%20Palace_l_386_579.jpg",
            "https://hblimg.mmtcdn.com/content/hubble/img/delhi/mmt/activities/m_activities_delhi_india_gate_1_l_442_663.jpg",
            "https://hblimg.mmtcdn.com/content/hubble/img/goa/mmt/activities/m_Fort%20Aguada_6_l_436_654.jpg",
            "https://hblimg.mmtcdn.com/content/hubble/img/jodhpur/mmt/activities/m_activities-jodhpur-mehrangarh-fort_l_400_640.jpg",
            "https://hblimg.mmtcdn.com/content/hubble/img/madurai/mmt/activities/m_activities-madurai-meenakshi-temple_l_400_640.jpg",
            "https://hblimg.mmtcdn.com/content/hubble/img/vadodara/mmt/activities/m_activities_vadodara_statue_of_unity_l_405_810.jpg",
            "https://hblimg.mmtcdn.com/content/hubble/img/parwanoo/mmt/activities/m_activities_parwanoo_kamakhya_devi_temple_kamali_ashram_l_370_493.jpg",
            "https://hblimg.mmtcdn.com/content/hubble/img/Igatpuri/mmt/activities/m_Trimbakeshwar%20Temple-1_l_418_557.jpg",
            "https://hblimg.mmtcdn.com/content/hubble/img/ujjain/mmt/activities/m_Shree%20Mahakaleshwar%20Temple-3_p_528_431.jpg",
            "https://hblimg.mmtcdn.com/content/hubble/img/pondicherry/mmt/activities/m_activities-pondicherry-promenade-beach_l_400_640.jpg",
            "https://hblimg.mmtcdn.com/content/hubble/img/mathura/mmt/activities/m_activities_mathura_prem_mandir_l_311_640.jpg",
            "https://hblimg.mmtcdn.com/content/hubble/img/srinagar/mmt/activities/m_activities_dal_lake_5_l_497_763.jpg",
            "https://hblimg.mmtcdn.com/content/hubble/img/delhi/mmt/activities/m_activities_delhi_akshardham_temple_l_418_627.jpg",
           
        ]
        
        categories = Category.objects.all()
        for title, content, img_url in zip(titles, contents, img_urls):
            category = random.choice(categories)
            Post.objects.create(title=title, content=content, img_url=img_url, category=category)

        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))