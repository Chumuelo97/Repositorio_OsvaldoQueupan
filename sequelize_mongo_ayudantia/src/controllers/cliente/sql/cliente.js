//modelo sql
import ClienteModel from '../../../models/cliente/sql.js';

const sqlCliente = {}

sqlCliente.crearCliente = async ( req, res, next) => {    
    try {
        const bdSelection = req.params.typeBd;

        if(bdSelection === 'sql'){
            
            await ClienteModel.create(req.body); //funciones de sequilize
           
            return res.status(200).json({
                success: true,
                message: "Cliente creado en sql"
            });
        };
        
        next();
        
    } catch (error) {
        console.log(error)
        return res.status(500).json({
            success: false,
            error
        });
    };
};

sqlCliente.listarClientes = async ( req, res, next) => {    
    try {
        const bdSelection = req.params.typeBd;

        if(bdSelection === 'sql'){
            
            const data = await ClienteModel.findAll(); //funciones de sequilize
            if(data.length > 0){
                return res.status(200).json({
                    success: true,
                    data,
                    message: "Clientes en sequelize"
                });
            };

            return res.status(404).json({
                success: false,
                message: "No hay clientes en bd sql"
            });
        };

        next();

    } catch (error) {
        console.log(error)
        return res.status(500).json({
            success: false,
            error
        });
    };
};

sqlCliente.listarById = async (req, res, next) => {
    try {
        const { typeBd, idCliente } = req.params;

        if( typeBd === 'sql' ){

            const cliente = await ClienteModel.findByPk( idCliente );
            
            if( cliente ){
                return res.status(200).json({
                    success: true,
                    cliente
                });
            };
            return res.status(404).json({
                success: false,
                error:"Cliente no encontrado"
            });
        };

        next();

    } catch ( error ) {
        console.log( error );
        return res.status(404).json({
            success: false,
            error:"Cliente no encontrado"
        });
    };
};

export default sqlCliente;