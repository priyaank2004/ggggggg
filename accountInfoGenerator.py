import string
import random


# Generating name functions 
# You can create different surnames to increase the variety of usernames.
def generatingName():
    firstName = ["Alan", "Murat", "Azad", "Necati", "Aaron", "Aaron-James", "Aarron", "Aaryan", "Aaryn", "Aayan",
                 "Aazaan", "Abaan", "Abbas", "Abdallah", "Abdalroof", "Abdihakim", "Abdirahman", "Abdisalam", "Abdul",
                 "Abdul-Aziz", "Abdulbasir", "Abdulkadir", "Abdulkarem", "Abdulkhader", "Abdullah", "Abdul-Majeed",
                 "Abdulmalik", "Abdul-Rehman", "Abdur", "Abdurraheem", "Abdur-Rahman", "Abdur-Rehmaan", "Abel",
                 "Abhinav", "Abhisumant", "Abid", "Abir", "Abraham", "Abu", "Abubakar", "Ace", "Adain", "Adam",
                 "Adam-James", "Addison", "Addisson", "Adegbola", "Adegbolahan", "Aden", "Adenn", "Adie", "Adil",
                 "Aditya", "Adnan", "Adrian", "Adrien", "Aedan", "Aedin", "Aedyn", "Aeron", "Afonso", "Ahmad", "Ahmed",
                 "Ahmed-Aziz", "Ahoua", "Ahtasham", "Aiadan", "Aidan", "Aiden", "Aiden-Jack", "Aiden-Vee", "Aidian",
                 "Aidy", "Ailin", "Aiman", "Ainsley", "Ainslie", "Airen", "Airidas", "Airlie", "AJ", "Ajay", "A-Jay",
                 "Ajayraj", "Akan", "Akram", "Al", "Ala", "Alan", "Alanas", "Alasdair", "Alastair", "Alber", "Albert",
                 "Albie", "Aldred", "Alec", "Aled", "Aleem", "Aleksandar", "Aleksander", "Aleksandr", "Aleksandrs",
                 "Alekzander", "Alessandro", "Alessio", "Alex", "Alexander", "Alexei", "Alexx", "Alexzander", "Alf",
                 "Alfee", "Alfie", "Alfred", "Alfy", "Alhaji", "Al-Hassan", "Ali", "Aliekber", "Alieu", "Alihaider",
                 "Alisdair", "Alishan", "Alistair", "Alistar", "Alister", "Aliyaan", "Allan", "Allan-Laiton", "Allen",
                 "Allesandro", "Allister", "Ally", "Alphonse", "Altyiab", "Alum", "Alvern", "Alvin", "Alyas", "Amaan",
                 "Aman", "Amani", "Ambanimoh", "Ameer", "Amgad", "Ami", "Amin", "Amir", "Ammaar", "Ammar", "Ammer",
                 "Amolpreet", "Amos", "Amrinder", "Amrit", "Amro", "Anay", "Andrea", "Andreas", "Andrei", "Andrejs",
                 "Andrew", "Andy", "Anees", "Anesu", "Angel", "Angelo", "Angus", "Anir", "Anis", "Anish", "Anmolpreet",
                 "Annan", "Anndra", "Anselm", "Anthony", "Anthony-John", "Antoine", "Anton", "Antoni", "Antonio",
                 "Antony", "Antonyo", "Anubhav", "Aodhan", "Aon", "Aonghus", "Apisai", "Arafat", "Aran", "Arandeep",
                 "Arann", "Aray", "Arayan", "Archibald", "Archie", "Arda", "Ardal", "Ardeshir", "Areeb", "Areez",
                 "Aref", "Arfin", "Argyle", "Argyll", "Ari", "Aria", "Arian", "Arihant", "Aristomenis", "Aristotelis",
                 "Arjuna", "Arlo", "Armaan", "Arman", "Armen", "Arnab", "Arnav", "Arnold", "Aron", "Aronas", "Arran",
                 "Arrham", "Arron", "Arryn", "Arsalan", "Artem", "Arthur", "Artur", "Arturo", "Arun", "Arunas", "Arved",
                 "Arya", "Aryan", "Aryankhan", "Aryian", "Aryn", "Asa", "Asfhan", "Ash", "Ashlee-jay", "Ashley",
                 "Ashton", "Ashton-Lloyd", "Ashtyn", "Ashwin", "Asif", "Asim", "Aslam", "Asrar", "Ata", "Atal",
                 "Atapattu", "Ateeq", "Athol", "Athon", "Athos-Carlos", "Atli", "Atom", "Attila", "Aulay", "Aun",
                 "Austen", "Austin", "Avani", "Averon", "Avi", "Avinash", "Avraham", "Awais", "Awwal", "Axel", "Ayaan",
                 "Ayan", "Aydan", "Ayden", "Aydin", "Aydon", "Ayman", "Ayomide", "Ayren", "Ayrton", "Aytug", "Ayub",
                 "Ayyub", "Azaan", "Azedine", "Azeem", "Azim", "Aziz", "Azlan", "Azzam", "Azzedine", "Babatunmise",
                 "Babur", "Bader", "Badr", "Badsha", "Bailee", "Bailey", "Bailie", "Bailley", "Baillie", "Baley",
                 "Balian", "Banan", "Barath", "Barkley", "Barney", "Baron", "Barrie", "Barry", "Bartlomiej", "Bartosz",
                 "Basher", "Basile", "Baxter", "Baye", "Bayley", "Beau", "Beinn", "Bekim", "Believe", "Ben", "Bendeguz",
                 "Benedict", "Benjamin", "Benjamyn", "Benji", "Benn", "Bennett", "Benny", "Benoit", "Bentley", "Berkay",
                 "Bernard", "Bertie", "Bevin", "Bezalel", "Bhaaldeen", "Bharath", "Bilal", "Bill", "Billy", "Binod",
                 "Bjorn", "Blaike", "Blaine", "Blair", "Blaire", "Blake", "Blazej", "Blazey", "Blessing", "Blue",
                 "Blyth", "Bo", "Boab", "Bob", "Bobby", "Bobby-Lee", "Bodhan", "Boedyn", "Bogdan", "Bohbi", "Bony",
                 "Bowen", "Bowie", "Boyd", "Bracken", "Brad", "Bradan", "Braden", "Bradley", "Bradlie", "Bradly",
                 "Brady", "Bradyn", "Braeden", "Braiden", "Brajan", "Brandan", "Branden", "Brandon", "Brandonlee",
                 "Brandon-Lee", "Brandyn", "Brannan", "Brayden", "Braydon", "Braydyn", "Breandan", "Brehme", "Brendan",
                 "Brendon", "Brendyn", "Breogan", "Bret", "Brett", "Briaddon", "Brian", "Brodi", "Brodie", "Brody",
                 "Brogan", "Broghan", "Brooke", "Brooklin", "Brooklyn", "Bruce", "Bruin", "Bruno", "Brunon", "Bryan",
                 "Bryce", "Bryden", "Brydon", "Brydon-Craig", "Bryn", "Brynmor", "Bryson", "Buddy", "Bully", "Burak",
                 "Burhan", "Butali", "Butchi", "Byron", "Cabhan", "Cadan", "Cade", "Caden", "Cadon", "Cadyn", "Caedan",
                 "Caedyn", "Cael", "Caelan", "Caelen", "Caethan", "Cahl", "Cahlum", "Cai", "Caidan", "Melim"]

    surName = ["Abak", "Demir", "Bala", "yilmaz", "Ediz",
               "yasar", "Ozbal", "Aydin", "kara",
               "Bakar", "Zengin", "Bilgin", "Kilic",
               "karabulut", "Abbas", "Hammoud", "Alan",
               "tilki", "Aslan", "Boz", "karaeski",
               "Deniz", "Temiz", "Alpaslan", "Demirci",
               "Erol", "Guneri", "yasin", "yelken",
               "Elmas", "Altin", "guller", "Bagci",
               "yucel", "korkmaz", "cetin","Dari",
               "Albayrak", "Tekin", "Yurtkulu", "Metin",
               "Suvari", "Kizilay", "Inan", "tasi", "Akdeniz",
               "Albagu", "alk", "Acu", "Altun", "Karagul",
               "Avkar", "Ayana", "Alagan", "Akar"]
    return ''.join(random.choice(firstName) + ' ' + random.choice(surName))


# Generating a username
def username(size=8, chars=string.ascii_lowercase + random.choice(['.', '_'])):
    word_list = [
        "Agaha", "Agne", "ileen", "Alice", "Amy", "Angela", "Beatrice", "Bridget", "Catherine", 
        "Cordelia", "Dorothy", "Edith", "Elizabethe", "Emery", "Emma", "Esther", "Florence", "Frances", 
        "Getrude", "Helen", "Irene", "Issabel", "Judith", "Lucy", "Margaret", "Martha", 
        "Mary", "Matilda", "Naomi", "Phyllis", "Rebecca", "Rosemary", "Sabina", "Silvester", "Sophia", 
        "Wiifred", "Abel", "Ace", "Ada", "Adam", "Adela", "Adelio", "Adolph", "Adonis", "Adora", 
        "Agatha", "Aggie", "Aida", "Ailish", "Aimee", "Alan", "Albert", "Albino", "Alex", 
        "Alexandra", "Alfred", "Ali", "Alice", "Alika", "Allie", "Aloha", "Alvin", "Amanda", 
        "i", "Amos", "Amy", "Anais", "Andra", "Andrew", "Andy", "Angl", "Angelica", "Anika", 
        "Anna", "Annie", "Anthony", "Apollo", "Aria", "Ariel", "Arista", "Arnold", 
        "Arid", "Asha", "Aster", "Astin", "Aurora", "Ava", "Baba", "Biley", "Baldy", 
        "Babi", "Barbara", "Barbie", "Barley", "Barney", "Baron", "Bail", "Baxter", "Beau", 
        "Bee", "Beck", "Becky", "Belita", "Bela", "elle", "Bencia", "Benny", "Berg", "Bessie", 
        "Bna", "Bianca", "Bibiane", "Billy", "Bingo", "Bishop", "Biss", "Blondie", "Bonita", "Bono", 
        "Bois", "Boss", "Bright", "Bruno", "Buk", "Buddy", "Bunny", "Caesar", "Caley", "Calix", 
        "Cala", "Callia", "Camilla", "Captan", "Cara", "Carmel", "Carmen", "Casey", "Catherine", 
        "Cecil", "Celestyn", "Celina", "Cha Ca", "Champ", "Charles", "Charlie", "Chase", "Chavi", 
        "Celsea", "Cherie", "Chilli", "Choe", "Chhissy", "Chubby", "Cinjdy", "Clara", "Clark", 
        "Caudia", "Cleo", "Cleta", "Cliff", "Coco", "Cody", "Colin", "Connie", "coo", "Corby", 
        "Coy", "Coote", "Crison", "Crispin", "Cystal", "Cutie", "Cyclonje", "Cyma", "Daisy", 
        "Dali", "Danika", "Darby", "Dara", "Dain", "Dario", "Darwin", "Dave", "David", "Dean", 
        "Della", "Delling", "Delphine", "Dennis", "Denver", "Derry", "Deva", "Dexter", "Diallo", 
        "Dick", "Dino", "Dixie", "Donna", "Doris", "Dorothy", "Doujglas", "Duke", "Dustin", "Dyllis", 
        "Eavan", "Ebony", "Echo", "Edan", "Edline", "Eden", "Edwjard", "Edwin", "Eilis", "Eldora", 
        "Elf", "Elin", "Elisha", "Elizabeth", "Elle", "Elroy", "Elsa", "Elvis", "Elysia", "Emilie", 
        "Eric", "Eris", "Eros", "Esteban", "Esther", "Eva", "Evan", "Eve", "Farrell", "Favian", 
        "Fedora", "Felice", "Felix", "Fella", "Fielio", "Filija", "Fleta", "Florence", "Floria", 
        "Forrest", "Freeman", "abriel", "Gali", "Gm", "Gemma", "George", "Gilbert", "Gili", 
        "Giovanni", "Gloria", "Goofy", "Grace", "Grania", "Gregory", "Haley", "Halona", "Happy", 
        "Harley", "Harmony", "Harold", "Harry", "Hba", "Helejn", "Helia", "Hera", "Hero", "Hestia", 
        "Hollis", "Honey", "Hope", "Hubert", "Hue", "Huey", "Ian", "Iliana", "Indira", "Ingrid", 
        "Irina", "Iris", "Isaac", "Isabel", "Isadra", "Isis", "Jace", "Jack", "Jackson", "Jaclyn", 
        "Jade", "Jane", "Jasmine", "Jasper", "Jeffrson", "Jjeffrey", "Jenifer", "Jennie", "Jeremy", 
        "Jericho", "Jerry", "Jess", "Jessica", "Jesie", "Jojjdie", "Johanna", "Jolly", "Jordan", "Joy", 
        "Jud", "Julia", "Juliana", "Juliet", "Jusin", "Kali", "Kara", "Karena", "Karis", "Kassia", 
        "Kate", "Kellan", "Kelley", "Kerri", "Kevin", "Kitty", "Klaus", "Kori", "Kuper", "Kyra", 
        "Lakia", "Lala", "Lamis", "Lani", "Lapy", "Lara", "Lavina", "Lee", "Leena", "Lelia", "Leo", 'Love'
        "Leopold", "Lev", "Lidia", "Lily", "Lina", "Linda", "Lisa", "Lloyd", "Lonnie", "Lottie", "Louis", 
        "Lowell", "Lucia", "Lucifer", "Lucy", "Lukas", "Luna", "Mabel", "Madonna", "Maggie", "Makaio", 
        "Malissa", "Malo", "Mana", "Mandelina", "Manon", "Marcia", "Margaret", "Mary", "Mathilda", 
        "Maya", "Melina", "Meriel", "Mickey", "Mighty", "Minnie", "Miranda", "Missy", "Misty", "Molly", 
        "Monet", "Monica", "Morris", "Muffin", "Mulan", "Murphy", "Nadia", "Nalo", "Nami", "Nana", 
        "Nani", "Naomi", "Nara", "Narcisse", "Navid", "Neal", "Neema", "Nero", "Nia", "Nicholas", 
        "Nicky", "Nina", "Odelia", "Olga", "Olive", "Oliver", "Oscar", "Pablo", "Paloma", "Pamela", 
        "Patrick", "Pavel", "Peggy", "Pello", "Penda", "Peppi", "Petra", "Phila", "Phillip", "Pinky", 
        "Pluto", "Poco", "Polo", "Pooky", "Poppy", "Primo", "Prince", "Princess", "Puffy", "Rabia", 
        "Raina", "Ralph", "Rambo", "Rania", "Ravi", "Redford", "Reggie", "Rei", "Remy", "Rex", "Richard", 
        "Ricky", "Ringo", "Rio", "Risa", "Robbie", "Robert", "Robin", "Rocky", "Roja", "Rollo", "Romeo", 
        "Rosie", "Roxy", "Roy", "Ruby", "Rudolph", "Rudy", "Ryan", "Sabrina", "Sally", "Salvatore", 
        "Sam", "Samson", "Sandy", "Sarah", "Sasha", "Scarlet", "Scoop", "Sebastian", "Selina", "Selma", 
        "Serena", "Severino", "Shaina", "Sasa", "Sheri", "Silky", "Simba", "Simon", "Sniper", "Solomon", 
        "Sonia", "Sonny", "Sophie", "Sora", "Sprky", "Spooky", "Spotty", "Stella", "Steven", "Sting", 
        "Storm", "Sugar", "Sunny", "Sweetie", "Sylvestr", "Sylvia", "Talia", "Talli", "Tanesia", 
        "Tania", "Ted", "Teenie", "Terra", "Tess", "Thomas", "Tomo", "Trisha", "Trudy", "Uba", 
        "Umberto", "Valencia", "Vnessa", "Veika", "Vra", "erdi", "Veronica", "Victoria", 
        "Vincent", "iolet", "Vito", "Vivi", "Waldo", "Walter", "Weenie", "Wendy", "William", 
        "Wily", "Winston", "Woody", "Yaro", "Yeti", "Yuki", "Zaza", "Zeki", "Zelia", "Zena", 
        "Zena", "Zenon", "Zeppelin", "Zeus", "Zili", "Zinna", "Zizi", "Zoe", "Zorro", "Zulu",
    ]
    word_list += chars

    result_username = 'x' * 100 # Init username as dummy words
    while len(result_username) < size or len(result_username) >= 30: ### Limit of instagram username length is 30
        ### Case 0: Combination of words
        n_word = random.randint(1,2)
        target_word_list = list(map(lambda x: x.lower(), random.choices(word_list , k=n_word)))

        ### Case 1: Flip each word (5%)
        for word_i, target_word in enumerate(target_word_list):
            if random.random() < 0.03:
                target_word = target_word[::-1] 
            target_word_list[word_i] = target_word

        ### Case 2: replace character to 'x' or 'y' or number (3%)
        for word_i, target_word in enumerate(target_word_list):
            for ch_i in range(len(target_word)):
                if random.random() < 0.03:
                    target_char = random.choice(['x', 'y']+list(map(str, range(10))))
                    target_word = target_word[:ch_i] + target_char + target_word[ch_i+1:] 
            target_word_list[word_i] = target_word

        ### Case 3: Repeat last character (7%, 1~4 times)
        for word_i, target_word in enumerate(target_word_list):
            # if random.random() < 0.07:
            #     target_word = (target_word[0]*random.randint(1,3)) + target_word 
            if random.random() < 0.07:
                target_word += (target_word[-1]*random.randint(1,4)) 
            target_word_list[word_i] = target_word

        ### Case 4: Join the words with '.' or '_'
        joining_char = random.choice(['.', '_'])
        result_username = joining_char.join(target_word_list)

        ### Case 5: Add some number to end (30%, 1~999999)
        if random.random() < 0.3:
            if random.random() < 0.6:
                result_username += joining_char
            additional_number_list = []
            number_list = list(map(str, range(10)))
            additional_number_list.append(random.choice(number_list))
            number_list += ['']*10
            additional_number_list += random.choices(number_list, k=5)
            result_username += ''.join(list(map(str, additional_number_list)))

    return result_username

# Generating a password
def getPassword(size=8, chars=string.ascii_lowercase + random.choice(['.', '_'])):
    return ''.join(random.choice(chars) for _ in range(size))


# Generating a Email
def generatingEmail():
    return ''.join(username() + '@mail.com')

if __name__=='__main__':
    print(username(size=12, chars=string.ascii_lowercase + random.choice(['.', '_'])))
