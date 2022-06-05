// import 'dotenv/config'
// require('dotenv').config();

export default {
    author : {
        name: process.env.VUE_APP_PROFILE_NAME,
        avatar: process.env.VUE_APP_PROFILE_AVATAR,
        url: process.env.VUE_APP_PROFILE_URL,
        social_media:{
            linkedin: process.env.VUE_APP_PROFILE_LINKEDIN,
            github: process.env.VUE_APP_PROFILE_GITHUB,
        },
        donate: process.env.VUE_APP_PROFILE_DONATE,
    },

    // ipfs: {
    //     host: 'ipfs.infura.io',
    //     port: 5001,
    //     protocol: 'https'
    // },
    // networks: {
    //     development: {
    //         host: 'localhost',
    //         port: 7545,
    //         network_id: "*" // Match any network id
    //     },
    //     ropsten: {
    //         provider: function() {
    //             return new HDWalletProvider(
    //                 privateKeys.split(','), // Array of account private keys
    //                 `https://ropsten.infura.io/v3/${process.env.INFURA_API_KEY}`// Url to an Ethereum Node
    //             )
    //         },
    //         gas: 5000000,
    //         gasPrice: 25000000000,
    //         network_id: 3
    //     }
    // },
    // contracts_directory: './contracts/',
    // contracts_build_directory: '../client/src/abis/',
    // compilers: {
    //     solc: {
    //         optimizer: {
    //             enabled: true,
    //             runs: 200
    //         }
    //     }
    // },
}
