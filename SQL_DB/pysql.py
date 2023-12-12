import psycopg2

class DB():

    def create_sdb(self, cur):
        cur.execute("""CREATE TABLE IF NOT EXISTS clients (
                    id SERIAL PRIMARY KEY, 
                    f_name VARCHAR(40) NOT NULL, 
                    l_name VARCHAR(40) NOT NULL, 
                    email VARCHAR(50) NOT NULL
        );""")
        cur.execute("""CREATE TABLE IF NOT EXISTS phones (
                    id SERIAL PRIMARY KEY,
                    client_id INT REFERENCES clients(id) NOT NULL,
                    phone VARCHAR(11) NOT NULL
        );""")
        return 'Таблица успешно создана.'
    

    def add_data(self, cur, fname, lname, email, phone=None):
        cur.execute('INSERT INTO clients (f_name, l_name, email) VALUES (%s, %s, %s) RETURNING id;', (fname, lname, email))
        id = cur.fetchone()[0]
        if phone is not None:
            self.add_pnumber(cur, id, phone)
        return f'Добавлен клиент с ID {id}'
    
    def add_pnumber(self, cur, clientid, phone):
        cur.execute('SELECT id FROM clients WHERE id = %s;', (clientid,))
        s_id = cur.fetchone()[0]
        if clientid != s_id:
            return f'Клиента с ID {id} не существует'
        else: 
            cur.execute('INSERT INTO phones (client_id, phone) VALUES (%s, %s);', (clientid, phone))
            return "Данные добавлены"
    
    def update_data(self, cur, c_id, fname=None, lname=None, email=None):
        cur.execute('SELECT * FROM clients WHERE id = %s', (c_id,))
        sc_id = cur.fetchone()
        if fname == None:
            fname = sc_id[1]
        if lname == None:
            lname = sc_id[2]
        if email == None:
            email = sc_id[3]
        cur.execute('UPDATE clients SET f_name = %s, l_name = %s, email = %s WHERE id = %s;', (fname, lname, email, c_id))
        
        return 'Данные обновлены'

    def update_phone(self, cur, p_id, c_id = None, phone = None):
        cur.execute("SELECT * FROM phones WHERE id = %s;", (p_id,))
        sp_id = cur.fetchone()
        if c_id == None:
            c_id = sp_id[1]
        if phone == None:
            phone = sp_id[2]
        cur.execute('UPDATE phones SET client_id = %s, phone = %s WHERE id = %s;', (c_id, phone, p_id))
        return 'Данные обновлены'

    def delete_phone(self, cur, phone):
        cur.execute('SELECT phone FROM phones WHERE phone = %s;', (phone,))
        s_phone = cur.fetchone()[0]
        if len(s_phone) == 0 or phone != s_phone:
            return f'Номер телефона {phone} нету'
        else:
            cur.execute('DELETE FROM phones WHERE phone = %s;', (phone,))
            return f'Номер телефона {phone} удален'
    
    def delete_client(self, cur, id):
        cur.execute('DELETE FROM phones WHERE client_id = %s;', (id,))
        cur.execute('DELETE FROM clients WHERE id = %s;', (id,))
        return 'Клиент удален'
    
    def find(self, cur, fname=None, lname=None, email=None, phone=None):
        if fname is not None:
            fname = f'%{fname}%'
        else: 
            fname = '%'
        if lname is not None:
            lname = f'%{lname}%'
        else:
            lname = '%'
        if email is not None:
            email = f'%{email}%'
        else:
            email = '%'
        if phone is not None:
            cur.execute("""SELECT c.id, c.f_name, c.l_name, c.email, p.phone FROM clients c
                        LEFT JOIN phones p ON c.id = p.client_id
                        WHERE c.f_name LIKE %s AND c.l_name LIKE %s AND c.email LIKE %s AND p.phone LIKE %s;
            """, (fname, lname, email, phone))
        else:
            cur.execute("""SELECT c.id, c.f_name, c.l_name, c.email, p.phone FROM clients c
                        LEFT JOIN phones p ON c.id = p.client_id
                        WHERE c.f_name LIKE %s AND c.l_name LIKE %s AND c.email LIKE %s;
            """, (fname, lname, email))
        return cur.fetchall()


with psycopg2.connect(database="test", user="postgres", password="robloxmaster123") as conn:
    with conn.cursor() as curs:
        post = DB()
        # Создания БД:
        # print(post.create_sdb(curs))
        # # Добавление клиентов:
        # print(post.add_data(curs, 'Rail', 'Gaifullin', 'r@mail.ru'))
        # print(post.add_data(curs, 'Madina', 'Zripov', 'z@gmail.ru', '89673454187'))
        # print(post.add_data(curs, 'Alex', 'Shardakov', 's@bk.ru', '12345678912'))
        # print(post.add_data(curs, 'Tasya', 'Volkovna', 't@yandex.ru'))
        # print(post.add_data(curs, 'Anyyya', 'Secret', 'a@mail.ru', '88734581731'))
        # # Добавление новых номеров:
        # print(post.add_pnumber(curs, 2, '3-62-71'))
        # print(post.add_pnumber(curs, 3, '84739812091'))
        # print(post.add_pnumber(curs, 5, '89437546122'))
        # # Обновление данных и номеров:
        # print(post.update_data(curs, 2, None, 'Zaripova', 'z@gmail.com'))
        # print(post.update_data(curs, 5, 'Anya'))
        # print(post.update_phone(curs, 2, None, '88078734192'))
        # print(post.update_phone(curs, 3, 4))
        # # Удаление номера:
        # print(post.delete_phone(curs, '89437546122'))
        # # Удаление клиента:
        # print(post.delete_client(curs, 3))
        # # Select запрос: 
        print(post.find(curs, 'Madina'))
        print(post.find(curs, None, 'Secret'))
        print(post.find(curs, None, None, None, '3-62-71'))

