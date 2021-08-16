const NAANJ_URL = "https://raw.githubusercontent.com/datadavev/naanj/main/data/naanj.json";

var NAANs = {};
var NAANi = {};

//Load NAANs from naanj
fetch(NAANJ_URL)
    .then(response => response.json())
    .then(data => {
        NAANs=data;
        for (var i=0; i < NAANs.naa.length; i++) {
            NAANi[NAANs.naa[i].what] = i;
        }
    });

//Lookup issuer given a NAAN
function getIssuer(naan) {
    let _naa = {"who":{"literal":"Not a NAA"}};
    let nidx = NAANi[naan];
    if (typeof nidx != "undefined") {
        _naa = NAANs.naa[nidx];
    }
    return _naa.who.literal;
}

//Split an ARK into pieces
function piecesOfARK(ark) {
    return window.__BRYTHON__.pyobj2jsobj(jsPiecesOfARK(ark));
}

//Initialization
document.addEventListener('alpine:init', () => {
    //siteinfo provides the footer text
    Alpine.data('siteinfo', () => ({
        _info: "",

        update() {
            const url = "https://api.github.com/repos/datadavev/SNARK/commits/main";
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    let _sha = data.sha.substr(0,7);
                    var dmod = data.commit.author.date;
                    this._info = "Revision " + _sha + " at " + dmod;
                })
        }
    }));

    // respond to changes in the input
    Alpine.data('ARK_data', () => ({
        input: "",
        inflection: "",
        pieces: {
            name: "",
            naan: "",
            qualifier: ""
        },
        issuer: "",
        lines: [],
        loading: true,

        init() {
          brython();
          this.loading = false;
        },

        update() {
            let res = window.__BRYTHON__.pyobj2jsobj(jsNormalizeARK(this.input));
            this.inflection = res.inflection;
            this.lines = res.result;
            this.pieces = piecesOfARK(res.result[res.result.length-1]);
            let _naa = {"who":{"literal":"Not a NAA"}};
            let nidx = NAANi[this.pieces.naan];
            if (typeof nidx != "undefined") {
                _naa = NAANs.naa[nidx];
            }
            this.issuer = getIssuer(this.pieces.naan);
        }
    }));
})

/*
function onLoad() {
    document.getElementById("results").style.display = "block";
    document.getElementById("snarker").style.display = "block";
}
*/
function onLoad() {

}