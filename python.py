class KnowledgeBase:
    def __init__(self):
        self.facts = []

    def add_fact(self, fact):
        self.facts.append(fact)

    def get_related_people(self, person, relation):
        related_people = []
        for fact in self.facts:
            if person == fact[0] and relation == fact[1]:
                related_people.append(fact[2])
        return related_people

# Create a knowledge base and add some facts
kb = KnowledgeBase()

kb.add_fact(("hadi", "adalah_orangtua_dari", "desi"))
kb.add_fact(("hadi", "adalah_orangtua_dari", "wahyu"))
kb.add_fact(("hadi", "adalah_orangtua_dari", "fathurrahman"))
kb.add_fact(("hadi", "adalah_orangtua_dari", "ardi"))
kb.add_fact(("alfian", "adalah_orangtua_dari", "desi"))
kb.add_fact(("alfian", "adalah_orangtua_dari", "wahyu"))
kb.add_fact(("alfian", "adalah_orangtua_dari", "fathurrahman"))
kb.add_fact(("alfian", "adalah_orangtua_dari", "ardi"))
kb.add_fact(("bayu", "adalah_orangtua_dari", "tari"))
kb.add_fact(("bayu", "adalah_orangtua_dari", "nurul"))
kb.add_fact(("bayu", "adalah_orangtua_dari", "yanto"))
kb.add_fact(("desi", "adalah_orangtua_dari", "tari"))
kb.add_fact(("desi", "adalah_orangtua_dari", "nurul"))
kb.add_fact(("desi", "adalah_orangtua_dari", "yanto"))
kb.add_fact(("fahrul", "adalah_orangtua_dari", "wanda"))
kb.add_fact(("tari", "adalah_orangtua_dari", "wanda"))
kb.add_fact(("ardi", "adalah_orangtua_dari", "eka"))
kb.add_fact(("ardi", "adalah_orangtua_dari", "mira"))
kb.add_fact(("ardi", "adalah_orangtua_dari", "bastian"))
kb.add_fact(("ana", "adalah_orangtua_dari", "eka"))
kb.add_fact(("ana", "adalah_orangtua_dari", "mira"))
kb.add_fact(("ana", "adalah_orangtua_dari", "bastian"))
kb.add_fact(("fathurrahman", "adalah_orangtua_dari", "hamzah"))
kb.add_fact(("nurul", "adalah_orangtua_dari", "aji"))
kb.add_fact(("nurul", "adalah_orangtua_dari", "gunawan"))
kb.add_fact(("mira", "adalah_orangtua_dari", "anggun"))
kb.add_fact(("mira", "adalah_orangtua_dari", "boy"))
kb.add_fact(("wahyu", "adalah_saudaralaki2_dari", "ardi"))
kb.add_fact(("ardi", "adalah_saudaralaki2_dari", "wahyu"))
kb.add_fact(("fahrul", "adalah_saudaralaki2_dari", "yanto"))
kb.add_fact(("yanto", "adalah_saudaralaki2_dari", "fahrul"))
kb.add_fact(("aji", "adalah_saudaralaki2_dari", "gunawan"))
kb.add_fact(("gunawan", "adalah_saudaralaki2_dari", "aji"))
kb.add_fact(("desi", "adalah_saudaraperempuan_dari", "fathurrahman"))
kb.add_fact(("fathurrahman", "adalah_saudaraperempuan_dari", "desi"))
kb.add_fact(("tari", "adalah_saudaraperempuan_dari", "nurul"))
kb.add_fact(("nurul", "adalah_saudaraperempuan_dari", "tari"))
kb.add_fact(("eka", "adalah_saudaraperempuan_dari", "mira"))
kb.add_fact(("mira", "adalah_saudaraperempuan_dari", "eka"))
kb.add_fact(("wahyu", "adalah_paman_dari", "tari"))
kb.add_fact(("wahyu", "adalah_paman_dari", "nurul"))
kb.add_fact(("wahyu", "adalah_paman_dari", "yanto"))
kb.add_fact(("wahyu", "adalah_paman_dari", "hamzah"))
kb.add_fact(("wahyu", "adalah_paman_dari", "eka"))
kb.add_fact(("wahyu", "adalah_paman_dari", "mira"))
kb.add_fact(("wahyu", "adalah_paman_dari", "bastian"))
kb.add_fact(("ardi", "adalah_paman_dari", "tari"))
kb.add_fact(("ardi", "adalah_paman_dari", "nurul"))
kb.add_fact(("ardi", "adalah_paman_dari", "yanto"))
kb.add_fact(("ardi", "adalah_paman_dari", "hamzah"))
kb.add_fact(("yanto", "adalah_paman_dari", "wanda"))
kb.add_fact(("bastian", "adalah_paman_dari", "anggun"))
kb.add_fact(("bastian", "adalah_paman_dari", "boy"))
kb.add_fact(("desi", "adalah_bibi_dari", "hamzah"))
kb.add_fact(("desi", "adalah_bibi_dari", "eka"))
kb.add_fact(("desi", "adalah_bibi_dari", "mira"))
kb.add_fact(("desi", "adalah_bibi_dari", "bastian"))
kb.add_fact(("fathurrahman", "adalah_bibi_dari", "tari"))
kb.add_fact(("fathurrahman", "adalah_bibi_dari", "nurul"))
kb.add_fact(("fathurrahman", "adalah_bibi_dari", "yanto"))
kb.add_fact(("fathurrahman", "adalah_bibi_dari", "eka"))
kb.add_fact(("fathurrahman", "adalah_bibi_dari", "mira"))
kb.add_fact(("fathurrahman", "adalah_bibi_dari", "bastian"))
kb.add_fact(("tari", "adalah_bibi_dari", "aji"))
kb.add_fact(("tari", "adalah_bibi_dari", "gunawan"))
kb.add_fact(("eka", "adalah_bibi_dari", "anggun"))
kb.add_fact(("eka", "adalah_bibi_dari", "boy"))
kb.add_fact(("nurul", "adalah_bibi_dari", "wanda"))
kb.add_fact(("hadi", "adalah_kakek_dari", "tari"))
kb.add_fact(("hadi", "adalah_kakek_dari", "nurul"))
kb.add_fact(("hadi", "adalah_kakek_dari", "yanto"))
kb.add_fact(("hadi", "adalah_kakek_dari", "hamzah"))
kb.add_fact(("hadi", "adalah_kakek_dari", "eka"))
kb.add_fact(("hadi", "adalah_kakek_dari", "mira"))
kb.add_fact(("hadi", "adalah_kakek_dari", "bastian"))
kb.add_fact(("bayu", "adalah_kakek_dari", "wanda"))
kb.add_fact(("bayu", "adalah_kakek_dari", "aji"))
kb.add_fact(("bayu", "adalah_kakek_dari", "gunawan"))
kb.add_fact(("ardi", "adalah_kakek_dari", "anggun"))
kb.add_fact(("ardi", "adalah_kakek_dari", "boy"))
kb.add_fact(("alfian", "adalah_nenek_dari", "tari"))
kb.add_fact(("alfian", "adalah_nenek_dari", "nurul"))
kb.add_fact(("alfian", "adalah_nenek_dari", "yanto"))
kb.add_fact(("alfian", "adalah_nenek_dari", "hamzah"))
kb.add_fact(("alfian", "adalah_nenek_dari", "eka"))
kb.add_fact(("alfian", "adalah_nenek_dari", "mira"))
kb.add_fact(("alfian", "adalah_nenek_dari", "bastian"))
kb.add_fact(("desi", "adalah_nenek_dari", "wanda"))
kb.add_fact(("desi", "adalah_nenek_dari", "aji"))
kb.add_fact(("desi", "adalah_nenek_dari", "gunawan"))
kb.add_fact(("tari", "adalah_sepupu_dari", "hamzah"))
kb.add_fact(("tari", "adalah_sepupu_dari", "eka"))
kb.add_fact(("tari", "adalah_sepupu_dari", "mira"))
kb.add_fact(("tari", "adalah_sepupu_dari", "bastian"))
kb.add_fact(("nurul", "adalah_sepupu_dari", "hamzah"))
kb.add_fact(("nurul", "adalah_sepupu_dari", "eka"))
kb.add_fact(("nurul", "adalah_sepupu_dari", "mira"))
kb.add_fact(("nurul", "adalah_sepupu_dari", "bastian"))
kb.add_fact(("yanto", "adalah_sepupu_dari", "hamzah"))
kb.add_fact(("yanto", "adalah_sepupu_dari", "eka"))
kb.add_fact(("yanto", "adalah_sepupu_dari", "mira"))
kb.add_fact(("yanto", "adalah_sepupu_dari", "bastian"))
kb.add_fact(("hamzah", "adalah_sepupu_dari", "tari"))
kb.add_fact(("hamzah", "adalah_sepupu_dari", "nurul"))
kb.add_fact(("hamzah", "adalah_sepupu_dari", "yanto"))
kb.add_fact(("hamzah", "adalah_sepupu_dari", "eka"))
kb.add_fact(("hamzah", "adalah_sepupu_dari", "mira"))
kb.add_fact(("hamzah", "adalah_sepupu_dari", "bastian"))
kb.add_fact(("eka", "adalah_sepupu_dari", "tari"))
kb.add_fact(("eka", "adalah_sepupu_dari", "nurul"))
kb.add_fact(("eka", "adalah_sepupu_dari", "yanto"))
kb.add_fact(("eka", "adalah_sepupu_dari", "hamzah"))
kb.add_fact(("mira", "adalah_sepupu_dari", "tari"))
kb.add_fact(("mira", "adalah_sepupu_dari", "nurul"))
kb.add_fact(("mira", "adalah_sepupu_dari", "yanto"))
kb.add_fact(("mira", "adalah_sepupu_dari", "hamzah"))
kb.add_fact(("bastian", "adalah_sepupu_dari", "tari"))
kb.add_fact(("bastian", "adalah_sepupu_dari", "nurul"))
kb.add_fact(("bastian", "adalah_sepupu_dari", "yanto"))
kb.add_fact(("bastian", "adalah_sepupu_dari", "hamzah"))
kb.add_fact(("wanda", "adalah_sepupu_dari", "aji"))
kb.add_fact(("wanda", "adalah_sepupu_dari", "gunawan"))



# Query
person = "bastian" #masukkan orang yang ingin di cari
relation ="adalah_sepupu_dari" #masukkan relasi yang ingin di cari 


related_people = kb.get_related_people(person, relation)

if related_people:
    print(f"{person} {relation} {', '.join(related_people)}")

else:
    print(f"No information found about {person} {relation}")
    