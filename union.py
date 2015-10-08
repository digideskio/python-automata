from graphviz import Digraph
from DFA import DFA, union

A1 = {
    "initial": 0,
    "final": [0],
    "alpha": ["a", "b"],
    "transitions": [
        [1, 2],
        [2, 0],
        [0, 1]
    ]
}
A2 = {
    "initial": 0,
    "final": [2],
    "alpha": ["a", "b"],
    "transitions": [
        [1, 2],
        [3, 2],
        [1, 2],
        [3, 3]
    ]
}


def delta_from_table(jdfa):
    res = {}
    alpha = jdfa['alpha']
    for i, transition in enumerate(jdfa['transitions']):
        for j, tgt in enumerate(transition):
            res[(i, alpha[j])] = tgt

    return lambda s, a: res[(s, a)]


def dfa_from_jdfa(jdfa):
    states = range(len(jdfa['transitions']))
    delta = delta_from_table(jdfa)

    return DFA(states, jdfa['alpha'], delta, jdfa['initial'], jdfa['final'])


def plot(dfa):
    dot = Digraph(comment='')

    for s in dfa.states:
        attrs = {'shape': 'circle'}
        if s == dfa.start:
            attrs['fillcolor'] = 'yellow'
        if s in dfa.accepts:
            attrs['shape'] = 'doublecircle'

        dot.node(str(s), **attrs)

    for s in dfa.states:
        for sym in dfa.alphabet:
            r = dfa.delta(s, sym)
            dot.edge(str(s), str(r), label=sym)

    return dot


def main():
    da1 = dfa_from_jdfa(A1)
    da2 = dfa_from_jdfa(A2)
    da3 = union(da1, da2)

    dot = plot(da3)
    print dot.source
    dot.render(view=True)


if __name__ == '__main__':
    main()
