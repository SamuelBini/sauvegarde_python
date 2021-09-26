const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

//VARIABLES
let Q = []
let Pl = []
let Qsort = []
let Plsort = []

const nbQ = 10000
const nbP = 100

/**
 *
 * @param {Int16Array} player
 * @return {Int16Array}
 */
function Qtrue(player) {
    return player.filter(elt => elt != '0').length
}
/**
 *
 * @param {Array} list
 */
function settings(list, ind) {
    Pl.push({
        'player': ind,
        'nbTrue': Qtrue(list),
        'qTrue': list.map((elt, i) => {
            if (elt != '0') return i + 1
        }).filter(elt => elt)
    })
    Plsort = [...Pl].sort((a, b) => a.nbTrue - b.nbTrue)
    list.forEach((elt, i) => {
        let noQ = i + 1
        if (ind == 1) {
            Q[i] = {
                'question': noQ,
                'nbTrue': parseInt(elt),
            }
        } else {
            Q[i] = {
                'question': noQ,
                'nbTrue': parseInt(elt) + parseInt(Q[i].nbTrue),
            }
        }

    })

    Qsort = [...Q].sort((a, b) => a.nbTrue - b.nbTrue)
}

function getFirst(tab, nb) {
    let temp = []
    for (let i = 0; i < nb; i++) {
        temp.push(tab[i])
    }
    return temp
}

function getDiffQ(Qtab, percent) {
    return Qtab.filter(elt => elt.nbTrue <= percent)
}

function nbQDbyPl(players, QDs) {
    let playersF = []
    players.forEach((pl, i) => {
        let nbQD = 0
        QDs.forEach((q, j) => {
            if (pl.qTrue.includes(q.question)) {
                nbQD++;
            }
        })
        playersF.push({
            'player': pl.player,
            'nbTrue': pl.nbTrue,
            'nbQD': nbQD
        })
    })
    return playersF

}

function playerCoef(eTrich, coefR, coefD) {
    let plCoef = []
    eTrich.forEach(trich => {
        plCoef.push({
            'player': trich.player,
            'nbTrue': trich.nbTrue,
            'coef': parseFloat(trich.nbTrue * coefR + trich.nbQD * coefD)
        })
    });
    return plCoef
}

function getTricheur(playerCoef) {
    let tricheur
    let max = 0
    playerCoef.forEach((pl, i) => {
        if (pl.coef > max) {
            tricheur = pl
            max = pl.coef
        }
    })
    return tricheur
}

function writeR(tricheur, cas) {
    console.log(`Case #${cas}: ${tricheur.player}`);
}

let curPlayer = 1
let curCas = 1


rl.question('', (T) => {
    let nbCas = parseInt(T)
    rl.question('', (P) => {
        rl.on('line', (L) => {
            let lTab = L.split('')
            settings(lTab, curPlayer)
            if (curPlayer === nbP) {
                let QDs = getDiffQ(Qsort.reverse(), 6)
                let first = getFirst(Plsort.reverse(), 10)
                let eTr = nbQDbyPl(first, QDs)
                let plCoef = playerCoef(eTr, 0.1, 0.9)
                let tricheur = getTricheur(plCoef)
                writeR(tricheur, curCas);
                if (curCas === nbCas) {
                    rl.close()
                } else {
                    Q = []
                    Pl = []
                    Qsort = []
                    Plsort = []
                    curPlayer = 0
                    curCas++
                }
            }
            curPlayer++
        })
    })
})