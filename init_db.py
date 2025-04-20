import sqlite3

def connect():
    return sqlite3.connect('database.db')

def criar_tabelas():
    conn = connect()
    c = conn.cursor()
   
    with open('schema.sql') as f:
      c.executescript(f.read())
   
    c.execute("""
      INSERT OR IGNORE INTO usuarios (nome, senha) VALUES (?, ?)
    """, ('admin', 'senha_admin'))
   
    c.execute("""
      INSERT OR IGNORE INTO usuarios (nome, senha) VALUES (?, ?)
    """, ('usuario1', 'senha_usuario1'))

    c.execute("""INSERT INTO contato (whatsapp, facebook, instagram, email, endereco) VALUES (?, ?, ?, ?, ?)
    """, ('+5519991626248', 'https://www.facebook.com', 'https://www.instagram.com', 'joaocsc@gmail.com', 'Americana - SP, 13472-000'))
   
    c.execute("""INSERT INTO mensagem_bottom (texto) VALUES (?)
    """, ('© 2025 Website desenvolvido por alunos da UNIVESP para o Projeto Integrador em Computação III.',))

    c.execute("""
      INSERT INTO textos (quem_somos, sobre_a_comunidade, transparencia) select ?, ?, ? where not exists(select * from textos)
    """, ('quem_somos_texto', 'sobre_a_comunidade', 'transparencia'))

    c.execute("""
      INSERT INTO promocao (nome, descricao, imagem) SELECT ?, ?, ? WHERE NOT EXISTS(SELECT * from promocao)
     """, ('Aguarde!', 'Em breve uma nova promoção', ''))

    c.execute("""
      DELETE FROM cliente
    """)

    c.execute("""
      INSERT OR IGNORE INTO cliente (nome, telefone, created) VALUES (?, ?, ?)
    """, ('Teste 0', '19991626248', '2025-04-01 13:49:57'))

    c.execute("""
      INSERT OR IGNORE INTO cliente (nome, telefone, created) VALUES (?, ?, ?)
    """, ('Teste 1', '19991626244', '2025-04-19 13:49:57'))

    c.execute("""
      INSERT OR IGNORE INTO cliente (nome, telefone, created) VALUES (?, ?, ?)
    """, ('Teste 2', '19991626245', '2025-04-19 13:49:57'))

    c.execute("""
      INSERT OR IGNORE INTO cliente (nome, telefone, created) VALUES (?, ?, ?)
    """, ('Teste 4', '19991626247', '2025-04-19 13:49:57'))

    c.execute("""
      INSERT OR IGNORE INTO cliente (nome, telefone, created) VALUES (?, ?, ?)
    """, ('Teste 6', '19991626249', '2025-04-16 13:49:57'))

    c.execute("""
      INSERT OR IGNORE INTO cliente (nome, telefone, created) VALUES (?, ?, ?)
    """, ('Teste 7', '19991626250', '2025-04-11 13:49:57'))

    c.execute("""
      INSERT OR IGNORE INTO cliente (nome, telefone, created) VALUES (?, ?, ?)
    """, ('Teste 8', '19991626251', '2025-04-02 13:49:57'))

    c.execute("""
      INSERT OR IGNORE INTO cliente (nome, telefone, created) VALUES (?, ?, ?)
    """, ('Teste 9', '19991626252', '2025-04-02 13:49:57'))

    c.execute("""
      INSERT OR IGNORE INTO cliente (nome, telefone, created) VALUES (?, ?, ?)
    """, ('Teste 10', '19991626253', '2025-04-02 13:49:57'))

    c.execute("""
      INSERT OR IGNORE INTO cliente (nome, telefone, created) VALUES (?, ?, ?)
    """, ('Teste 11', '19991626254', '2025-04-02 13:49:57'))

    c.execute("""
      INSERT OR IGNORE INTO cliente (nome, telefone, created) VALUES (?, ?, ?)
    """, ('Teste 13', '19991626256', '2025-04-08 13:49:57'))

    c.execute("""
      INSERT OR IGNORE INTO cliente (nome, telefone, created) VALUES (?, ?, ?)
    """, ('Teste 14', '19991626258', '2025-04-03 13:49:57'))

    c.execute("""
      INSERT OR IGNORE INTO cliente (nome, telefone, created) VALUES (?, ?, ?)
    """, ('Teste 15', '19991626259', '2025-04-03 13:49:57'))
    
    conn.commit()
    conn.close()

