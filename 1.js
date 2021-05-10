function fromUntil(a) {
    /*2 Zahlen sollen ein ordentlicher Zahlenbereich sein, sonst werden sie es

    @rtype: tuple[int,int]
    @return: Eine Bereichsangabe
    */
    var swap;
    if (a[0].isdecimal()) {
        a[0] = Number.parseInt(a[0]);
        if (((a.length === 2) && a[1].isdecimal())) {
            a[1] = Number.parseInt(a[1]);
        } else {
            if ((a.length === 1)) {
                swap = a[0];
                a[0] = 1;
                a += [swap];
                a[0] = 1;
            } else {
                return [1, 1];
            }
        }
        return tuple(a);
    } else {
        return [1, 1];
    }
}

//# sourceMappingURL=toJS.js.map
