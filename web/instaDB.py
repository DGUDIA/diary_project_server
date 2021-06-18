happy = (('happy', 'https://www.instagram.com/p/CPx0_kvFuyB/embed/'),
         ('happy', 'https://www.instagram.com/p/CP2XE0GJwLM/embed/'),
        ('happy', 'https://www.instagram.com/p/CP4WfO5pJeW/embed/'),
        ('happy', 'https://www.instagram.com/p/CP3Qix1NTUH/embed/'),
        ('happy', 'https://www.instagram.com/p/CAFosinFvkz/embed/'),
        ('happy', 'https://www.instagram.com/p/CQN6CF3Fwbt/embed/'),
         ('happy', 'https://www.instagram.com/p/CQLrHM1F1YI/embed/'),
        ('happy', 'https://www.instagram.com/p/CQKrmJ3MfBE/embed/'),
        ('happy', 'https://www.instagram.com/p/CQNQ6npN0Bu/embed/'),
        ('happy', 'https://www.instagram.com/p/CQLVjOktcn9/embed/'))

sad = (('sad', 'https://www.instagram.com/p/CFUcN4glngh/embed/'),
('sad', 'https://www.instagram.com/p/CFUpPLmlngN/embed/'),
('sad', 'https://www.instagram.com/p/CP3GuiHHpUZ/embed/'),
('sad', 'https://www.instagram.com/p/CPp69eylhxt/embed/'),
('sad', 'https://www.instagram.com/p/CP4OSdzFu5o/embed/'),
('sad', 'https://www.instagram.com/p/CP4IpEKFaUs/embed/'),
('sad', 'https://www.instagram.com/p/CP3mOOYlhbN/embed/'),
('sad', 'https://www.instagram.com/p/CP3R7CYhDkl/embed/'),
('sad', 'https://www.instagram.com/p/CJdwBxAMVw9/embed/'),
('sad', 'https://www.instagram.com/p/CD0-kgaBJ1Y/embed/'))

angry = (('angry', 'https://www.instagram.com/p/CPsbGZ4F4_O/embed/'),
('angry', 'https://www.instagram.com/p/CPxb6n0FI7V/embed/'),
('angry', 'https://www.instagram.com/p/CPxPgwhMpGn/embed/'),
('angry', 'https://www.instagram.com/p/CHjY2EyAe9-/embed/'),
('angry', 'https://www.instagram.com/p/CPybfd6FZ_E/embed/'),
('angry', 'https://www.instagram.com/p/CMPXOjZnHxw/embed/'),
('angry', 'https://www.instagram.com/p/B-RFLbnlS7Q/embed/'),
('angry', 'https://www.instagram.com/p/CKQKuwop8DB/embed/'),
('angry', 'https://www.instagram.com/p/COPlfVOnGYt/embed/'),
('angry', 'https://www.instagram.com/p/CLrXu_7FJuw/embed/'))
 

neutral = (('neutral', 'https://www.instagram.com/p/CP4tZniH8KM/embed/'),
('neutral', 'https://www.instagram.com/p/CP4s5fPnVXE/embed/'),
('neutral', 'https://www.instagram.com/p/CP1tdAkLhH2/embed/'),
('neutral', 'https://www.instagram.com/p/CP2MImjHM5S/embed/'),
('neutral', 'https://www.instagram.com/p/CQLBFRVFjZv/embed/'),
('neutral', 'https://www.instagram.com/p/CP7fNXNlkGd/embed/'),
('neutral', 'https://www.instagram.com/p/CP5NDv7nB_z/embed/'),
('neutral', 'https://www.instagram.com/p/CPdFRjIFWu2/embed/'),
('neutral', 'https://www.instagram.com/p/CP8AtfbHzie/embed/'),
('neutral', 'https://www.instagram.com/p/CP24nr-Bdm2/embed/')) 
 
anxious = (('anxious', 'https://www.instagram.com/p/CPvPDDMlm1K/embed/'),
('anxious', 'https://www.instagram.com/p/CP4EaGrtjHZ/embed/'),
('anxious', 'https://www.instagram.com/p/CP2XE0GJwLM/embed/'),
('anxious', 'https://www.instagram.com/p/CP3Qix1NTUH/embed/'),
('anxious', 'https://www.instagram.com/p/CE8w54tF0fe/embed/'),
('anxious', 'https://www.instagram.com/p/CHm-Pg0nZb3/embed/'),
('anxious', 'https://www.instagram.com/p/CLtZ4AEpH0P/embed/'),
('anxious', 'https://www.instagram.com/p/CEJGpHunR8L/embed/'),
('anxious', 'https://www.instagram.com/p/BwZE1wbH98N/embed/'),
('anxious', 'https://www.instagram.com/p/CPiQjbpF09T/embed/'))

link_list = (happy + sad + neutral + anxious + angry)

def create_insta():
    import sqlite3

    conn = sqlite3.connect("instagram.db", isolation_level=None)
    c = conn.cursor()
    
    c.execute("CREATE TABLE IF NOT EXISTS instadb \
        (feeling text, link text)")
    
    c.executemany("INSERT INTO instadb (feeling, link) \
                VALUES(?,?)", link_list)

    conn.commit()
    
    conn.close()
    
create_insta()