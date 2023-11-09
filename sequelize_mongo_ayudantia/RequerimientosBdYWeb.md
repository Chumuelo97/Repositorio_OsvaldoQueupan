Descripción de Tablas
Direccion

Direcciones para clientes y comercios.
Persona

Información sobre los clientes.
FormaDePago

Distintas formas de pago que se pueden utilizar.
TipoRegistro

Tipos de registro para las personas (Cliente, Vendedor, etc.).
Pedido

Información sobre los pedidos realizados.
Pago

Detalles sobre los pagos realizados.
VersionProducto

Diferentes versiones o variantes de un producto.
Producto

Información sobre los productos disponibles.
Comercio

Información sobre los comercios.
Sucursal

Información sobre las sucursales de un comercio.
ProductoDisponibleSucursal

Relación entre productos y las sucursales donde están disponibles.
Vendedor

Información sobre los vendedores.
Relaciones
Persona y Direccion - 1 a M
Pedido y Persona (como Cliente) - 1 a M
Pedido y Vendedor - 1 a M
Pago y FormaDePago - M a 1
Pedido y Pago - 1 a M
Producto y VersionProducto - 1 a M
Comercio y Sucursal - 1 a M
Sucursal y ProductoDisponibleSucursal - 1 a M
Producto y ProductoDisponibleSucursal - 1 a M
Código SQL
Ten en cuenta que esto es un ejemplo básico y podría necesitar ajustes para cumplir con requisitos específicos.


-- Tabla Direccion
CREATE TABLE Direccion (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Calle VARCHAR(255),
    Ciudad VARCHAR(255),
    Comuna VARCHAR(255),
    Estado VARCHAR(50),
    Numero INT,
    OtroDatoDireccion TEXT,
    Region VARCHAR(255),
    ClienteID INT,
    ComercioID INT,
    SucursalID INT,
    PedidoID INT,
    FOREIGN KEY (ClienteID) REFERENCES Persona(ID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (ComercioID) REFERENCES Comercio(ID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (SucursalID) REFERENCES Sucursal(ID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (PedidoID) REFERENCES Pedido(ID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Tabla Persona
CREATE TABLE Persona (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    TipoRegistroID INT,
    -- Otros campos
    FOREIGN KEY (TipoRegistroID) REFERENCES TipoRegistro(ID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Tabla FormaDePago
CREATE TABLE FormaDePago (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(255)
);

-- Tabla TipoRegistro
CREATE TABLE TipoRegistro (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Tipo VARCHAR(255)
);

-- Tabla Pedido
CREATE TABLE Pedido (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    ClienteID INT,
    VendedorID INT,
    Estado VARCHAR(50),
    FechaDespacho DATE,
    FechaPedido DATE,
    DetallesAdicionales TEXT,
    FOREIGN KEY (ClienteID) REFERENCES Persona(ID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (VendedorID) REFERENCES Vendedor(ID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Tabla Pago
CREATE TABLE Pago (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    PedidoID INT,
    FormaPagoID INT,
    CodigoAutorizacion VARCHAR(50),
    Estado VARCHAR(50),
    FechaPago DATE,
    MontoPago DECIMAL(10, 2),
    FOREIGN KEY (PedidoID) REFERENCES Pedido(ID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (FormaPagoID) REFERENCES FormaDePago(ID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Tabla VersionProducto
CREATE TABLE VersionProducto (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    ProductoID INT,
    -- Otros campos
    FOREIGN KEY (ProductoID) REFERENCES Producto(ID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Tabla Producto
CREATE TABLE Producto (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(255),
    -- Otros campos
);

-- Tabla Comercio
CREATE TABLE Comercio (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(255),
    EmailComercio VARCHAR(255),
    Telefono VARCHAR(20),
    Estado VARCHAR(50)
);

-- Tabla Sucursal
CREATE TABLE Sucursal (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    ComercioID INT,
    DireccionID INT,
    CelularSucursal VARCHAR(20),
    EmailSucursal VARCHAR(255),
    TelefonoSucursal VARCHAR(20),
    FOREIGN KEY (ComercioID) REFERENCES Comercio(ID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (DireccionID) REFERENCES Direccion(ID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Tabla ProductoDisponibleSucursal
CREATE TABLE ProductoDisponibleSucursal (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    ProductoID INT,
    SucursalID INT,
    FOREIGN KEY (ProductoID) REFERENCES Producto(ID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (SucursalID) REFERENCES Sucursal(ID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Tabla Vendedor
CREATE TABLE Vendedor (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(255),
    -- Otros campos
 );
