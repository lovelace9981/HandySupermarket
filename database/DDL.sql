CREATE TABLE IF NOT EXISTS PASILLOS (
	COD_QR_PASILLO VARCHAR(150) NOT NULL,
	NOMBRE_PASILLO VARCHAR(40),
	DESCRIPCION VARCHAR(200),
	PHOTO_LOCATION VARCHAR(200),

	CONSTRAINT PK_COD_QR_PASILLO PRIMARY KEY (COD_QR_PASILLO)
);

CREATE TABLE IF NOT EXISTS ESTANTES (
	COD_QR_ESTANTE VARCHAR(150) NOT NULL,
	COD_QR_PASILLO VARCHAR(150),

	CONSTRAINT PK_COD_QR_ESTANTE PRIMARY KEY (COD_QR_ESTANTE),
	CONSTRAINT FK_COD_QR_PASILLO FOREIGN KEY (COD_QR_PASILLO) REFERENCES PASILLOS(COD_QR_PASILLO)
);

CREATE TABLE IF NOT EXISTS PRODUCTOS (
	COD_BARRAS_EAN_13 INT(13) NOT NULL,
	COD_QR_ESTANTE VARCHAR(150) NOT NULL,
	PRECIO DECIMAL(3,2),
	STOCK SMALLINT(2),
	INFORMACION_NUTRICIONAL VARCHAR(300),
	ALERGENOS VARCHAR(200),
	TAG_ALTERNATIVAS VARCHAR(10),
	PHOTO_LOCATION VARCHAR(200),

	CONSTRAINT PK_COD_BARRAS_EAN_13 PRIMARY KEY (COD_BARRAS_EAN_13),
	CONSTRAINT FK_COD_QR_ESTANTE FOREIGN KEY (COD_QR_ESTANTE) REFERENCES ESTANTES(COD_QR_ESTANTE),
	CONSTRAINT CHK_BAR_CODE CHECK(COD_BARRAS_EAN_13 REGEXP '[0-9]{13}')
);

CREATE TABLE IF NOT EXISTS CLIENTES (
	ID_CLIENTE INT(100) ZEROFILL NOT NULL,
	NOMBRE VARCHAR(10),
	APELLIDOS VARCHAR(10),
	DOMICILIO VARCHAR(10),

	CONSTRAINT PK_ID_CLIENTE PRIMARY KEY (ID_CLIENTE)
);

CREATE TABLE IF NOT EXISTS COMPRAS (
	ID_COMPRA INT (100) ZEROFILL NOT NULL,
	COD_BARRAS_EAN_13 INT(13),
	ID_CLIENTE INT(100) ZEROFILL,
	CANTIDAD_PRODUCTO TINYINT(2),
	PRECIO_TOTAL DECIMAL(3,2),
	FECHA_COMPRA DATE,

	CONSTRAINT PK_ID_COMPRA PRIMARY KEY (ID_COMPRA),
	CONSTRAINT FK_COD_BARRAS_EAN_13 FOREIGN KEY (COD_BARRAS_EAN_13) REFERENCES PRODUCTOS(COD_BARRAS_EAN_13),
	CONSTRAINT FK_ID_CLIENTE FOREIGN KEY (ID_CLIENTE) REFERENCES CLIENTES(ID_CLIENTE)
);