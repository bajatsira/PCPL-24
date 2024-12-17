edge(a, b).
edge(a, c).
edge(b, d).
edge(c, d).
edge(d, e).
edge(c, f).

path(Start, End, Path) :- % Путь между двумя вершинами
    travel(Start, End, [Start], Path).

travel(Start, End, Visited, [Start|Path]) :-
    edge(Start, Next),
    \+ member(Next, Visited),
    (   Next = End
    ->  Path = [End]
    ;   travel(Next, End, [Next|Visited], Path)
    ).

% ?- path(a, e, Path).
% Path = [a, c, d, e].

% ?- path(a, f, Path).
% Path = [a, c, f].
