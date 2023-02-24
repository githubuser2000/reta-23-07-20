console.log("Hello World!");
/*
function isZeilenAngabe(g) {
  let pattern = new RegExp("^v?[0-9-]+[\\+0-9,-]*$");
  return (
    pattern.test(g) &&
    !["-", "+"].includes(g.slice(-1)) &&
    !g.includes("--") &&
    !g.includes("++") &&
    !g.includes("+-") &&
    !g.includes("-+") &&
    !g.includes(",+") &&
    !g.includes("+,") &&
    !g.includes("-,")
  );
}
*/
function isZeilenAngabe(g) {
  const x = (g.match(/[0-9]+\-[0-9]+/g) || []).length;
  const y = (g.match(/[0-9]+\-[0-9]+\-[0-9]+/g) || []).length;
  return (
    /^(v?[0-9-]+[\+0-9,]*)$/.test(g) &&
    !["-", "+"].includes(g.slice(-1)) &&
    ((x < 2 && y == 0) || (/^v?\-?[0-9]+[\+0-9,]*$/.test(g) && x == 0)) &&
    !/--|\+\+|\+\-|\-\+|,\+|\+,|-,/.test(g)
  );
}

function BereichToNumbers2(MehrereBereiche, vielfache = false, maxZahl = 1028) {
  if (MehrereBereiche.length > 0 && MehrereBereiche[0] === "v") {
    MehrereBereiche = MehrereBereiche.slice(1);
    vielfache = true;
  }

  if (!isZeilenAngabe(MehrereBereiche)) {
    return new Set();
  }

  if (!vielfache && maxZahl === 0) {
    maxZahl = Infinity;
  }

  const Bereiche = MehrereBereiche.split(",");
  const dazu = new Set();
  const hinfort = new Set();
  let menge;

  for (const EinBereich of Bereiche) {
    BereichToNumbers2_EinBereich(EinBereich, dazu, hinfort, maxZahl, vielfache);
  }

  return new Set([...dazu].filter((x) => !hinfort.has(x)));
}

function BereichToNumbers2_EinBereich(
  EinBereich,
  dazu,
  hinfort,
  maxZahl,
  vielfache
) {
  if (EinBereich.length > 1 && EinBereich[0] === "-") {
    EinBereich = EinBereich.substring(1);
    menge = hinfort;
  } else if (EinBereich.length > 0 && EinBereich[0] !== "-") {
    menge = dazu;
  } else {
    menge = null;
  }

  const around = [];
  if (menge !== null) {
    const BereichTuple2 = EinBereich.split("+");
    if (EinBereich.match(/^\d+$/)) {
      EinBereich = EinBereich + "-" + EinBereich;
    } else if (BereichTuple2.length > 0 && BereichTuple2[0].match(/^\d+$/)) {
      EinBereich = BereichTuple2[0] + "-" + BereichTuple2[0];
      if (BereichTuple2.length > 1) {
        EinBereich += "+" + BereichTuple2.slice(1).join("+");
      }
    }
    const BereichCouple = EinBereich.split("-");
    BereichToNumbers2_EinBereich_Menge(
      BereichCouple,
      around,
      maxZahl,
      menge,
      vielfache
    );
  }
}

function BereichToNumbers2_EinBereich_Menge(
  BereichCouple,
  around,
  maxZahl,
  menge,
  vielfache
) {
  if (
    BereichCouple.length == 2 &&
    /^\d+$/.test(BereichCouple[0]) &&
    BereichCouple[0] != "0"
  ) {
    let BereichPlusTuples = BereichCouple[1].split("+");
    if (BereichPlusTuples.length < 2) {
      around = [0];
    } else {
      let richtig = true;
      let numList = [];
      for (let i = 0; i < BereichPlusTuples.length; i++) {
        if (/^\d+$/.test(BereichPlusTuples[i])) {
          numList.push(parseInt(BereichPlusTuples[i]));
        } else {
          richtig = false;
        }
      }
      if (richtig && numList.length > 0) {
        around = numList.slice(1);
        BereichCouple[1] = numList[0];
      }
    }
    if (vielfache) {
      BereichToNumbers2_EinBereich_Menge_vielfache(
        BereichCouple,
        around,
        maxZahl,
        menge
      );
    } else {
      BereichToNumbers2_EinBereich_Menge_nichtVielfache(
        BereichCouple,
        around,
        maxZahl,
        menge
      );
    }
  }
}

function BereichToNumbers2_EinBereich_Menge_vielfache(
  BereichCouple,
  around,
  maxZahl,
  menge
) {
  let i = 0;
  if (around.length === 0 || new Set(around).has(0)) {
    while (around.every((a) => parseInt(BereichCouple[0]) * i < maxZahl - a)) {
      i += 1;
      for (
        let number = parseInt(BereichCouple[0]);
        number <= parseInt(BereichCouple[1]);
        number++
      ) {
        for (const a of around) {
          const c = number * i;
          if (c <= maxZahl) {
            menge.add(c);
          }
        }
      }
    }
  } else {
    while (around.every((a) => parseInt(BereichCouple[0]) * i < maxZahl - a)) {
      i += 1;
      for (
        let number = parseInt(BereichCouple[0]);
        number <= parseInt(BereichCouple[1]);
        number++
      ) {
        for (const a of around) {
          const c = number * i + a;
          if (c <= maxZahl) {
            menge.add(c);
          }
          const d = number * i - a;
          if (d > 0 && d < maxZahl) {
            menge.add(d);
          }
        }
      }
    }
  }
}
function BereichToNumbers2_EinBereich_Menge_nichtVielfache(
  BereichCouple,
  around,
  maxZahl,
  menge
) {
  for (
    let number = parseInt(BereichCouple[0]);
    number <= parseInt(BereichCouple[1]);
    number++
  ) {
    for (let a of around) {
      let c = number + a;
      if (c < maxZahl) {
        menge.add(c);
      }
      let d = number - a;
      if (d > 0 && d < maxZahl) {
        menge.add(d);
      }
    }
  }
}
module.exports = {
  isZeilenAngabe: isZeilenAngabe,
  BereichToNumbers2: BereichToNumbers2,
  BereichToNumbers2_EinBereich: BereichToNumbers2_EinBereich,
  BereichToNumbers2_EinBereich_Menge: BereichToNumbers2_EinBereich_Menge,
  BereichToNumbers2_EinBereich_Menge_vielfache:
    BereichToNumbers2_EinBereich_Menge_vielfache,
  BereichToNumbers2_EinBereich_Menge_nichtVielfache:
    BereichToNumbers2_EinBereich_Menge_nichtVielfache,
};
