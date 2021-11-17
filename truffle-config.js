const { alice } = require('./scripts/sandbox/accounts');

module.exports = {
  // see <http://truffleframework.com/docs/advanced/configuration>
  // for more details on how to specify configuration options!
  networks: {
    development: {
      host: "http://localhost",
      port: 8732,
      network_id: "*",
      secretKey: alice.sk,
      type: "tezos"
    },
    mainnet: {
      host: "https://mainnet.smartpy.io",
      port: 443,
      network_id: "*",
      type: "tezos"
    },
    granadanet: {
      host: "https://granadanet.smartpy.io",
      port: 443,
      network_id: "*",
      type: "tezos"
    },
    hangzhounet: {
      host: "https://hangzhounet.smartpy.io",
      port: 443,
      network_id: "*",
      type: "tezos"
    }
  }
};
