from linked_list import Node, LinkedList
 
 
songs = [
    ('Blinding Lights', 'The Weeknd', 'After Hours'),
    ('As It Was', 'Harry Styles', "Harry's House"),
    ('Stay', 'The Kid LAROI & Justin Bieber', 'F*CK LOVE 3'),
    ('Levitating', 'Dua Lipa', 'Future Nostalgia'),
    ('Peaches', 'Justin Bieber', 'Justice'),
    ('Good 4 U', 'Olivia Rodrigo', 'SOUR'),
    ('Montero', 'Lil Nas X', 'Montero'),
    ('Heat Waves', 'Glass Animals', 'Dreamland'),
    ('Bad Habits', 'Ed Sheeran', '='),
    ('Industry Baby', 'Lil Nas X & Jack Harlow', 'Montero'),
    ('Shivers', 'Ed Sheeran', '='),
    ('Happier Than Ever', 'Billie Eilish', 'Happier Than Ever'),
    ('Butter', 'BTS', 'Butter'),
    ('Kiss Me More', 'Doja Cat & SZA', 'Planet Her'),
    ('Save Your Tears', 'The Weeknd', 'After Hours'),
    ('Watermelon Sugar', 'Harry Styles', 'Fine Line'),
    ('Drivers License', 'Olivia Rodrigo', 'SOUR'),
    ('Telepatia', 'Kali Uchis', 'Sin Miedo'),
    ('Therefore I Am', 'Billie Eilish', 'Therefore I Am'),
    ('Positions', 'Ariana Grande', 'Positions'),
    ('Leave The Door Open', 'Bruno Mars & Anderson .Paak', 'An Evening with Silk Sonic'),
    ('Dynamite', 'BTS', 'BE'),
    ('Mood', '24kGoldn ft. iann dior', 'El Dorado'),
    ('Traitor', 'Olivia Rodrigo', 'SOUR'),
    ('Enemy', 'Imagine Dragons & Arcane', 'Mercury Act 1'),
    ('Stereo Hearts', 'Gym Class Heroes', 'The Papercut Chronicles II'),
    ('Anti-Hero', 'Taylor Swift', 'Midnights'),
    ('Cruel Summer', 'Taylor Swift', 'Lover'),
    ('Flowers', 'Miley Cyrus', 'Endless Summer Vacation'),
    ('Unholy', 'Sam Smith & Kim Petras', 'Gloria'),
    ('Escapism', 'RAYE & 070 Shake', 'My 21st Century Blues'),
    ('Creepin', 'Metro Boomin & The Weeknd', 'Heroes & Villains'),
    ('Quevedo Bzrp', 'Bizarrap & Quevedo', 'Music Sessions Vol. 52'),
    ('Titi Me Pregunto', 'Bad Bunny', 'Un Verano Sin Ti'),
    ('Me Porto Bonito', 'Bad Bunny & Chencho Corleone', 'Un Verano Sin Ti'),
    ('Efecto', 'Bad Bunny', 'Un Verano Sin Ti'),
    ('La Bebe', 'Yng Lvcas & Peso Pluma', 'La Bebe'),
    ('Ella Baila Sola', 'Eslabon Armado & Peso Pluma', 'Ella Baila Sola'),
    ('El Azul', 'Junior H & Peso Pluma', 'El Azul'),
    ('Shakira Bzrp', 'Bizarrap & Shakira', 'Music Sessions Vol. 53'),
    ('TQG', 'Karol G & Shakira', 'Mañana Será Bonito'),
    ('Mañana Será Bonito', 'Karol G', 'Mañana Será Bonito'),
    ('PROVENZA', 'Karol G', 'KG0516'),
    ('La Fama', 'Rosalia & The Weeknd', 'El Madlenu'),
    ('Despecha', 'Rosalia', 'Motomami'),
    ('Bzrp & Nicki Nicole', 'Bizarrap & Nicki Nicole', 'Music Sessions Vol. 13'),
    ('Ojitos Lindos', 'Bad Bunny & Bomba Estéreo', 'Un Verano Sin Ti'),
    ('Todo de Ti', 'Rauw Alejandro', 'Vice Versa'),
    ('Pepas', 'Farruko', 'La 167'),
    ('Si Antes Te Hubiera Conocido', 'Karol G', 'Mañana Será Bonito'),
]
 
 
def build_playlist() -> LinkedList:
    playlist = LinkedList()
    for song, artist, album in songs:
        node = Node(song, artist, album)
        playlist.insert_at_end(node)
    return playlist