quadratic_roots(A, B, C, Roots) :-
    (   A =:= 0
    ->  (   B =\= 0
            ->  
                Root is -C / B,
                Roots = [Root]
            ;  
                (C =\= 0 -> Roots = [] ; Roots = [inf])
        )
    ;  
        Discriminant is B * B - 4 * A * C,
        (   Discriminant > 0
        ->  Root1 is (-B + sqrt(Discriminant)) / (2 * A),
            Root2 is (-B - sqrt(Discriminant)) / (2 * A),
            Roots = [Root1, Root2]
        ;   Discriminant =:= 0
        ->  Root is -B / (2 * A),
            Roots = [Root]
        ;   % Если дискриминант меньше 0
            Roots = []
        )
    ).


% ?- quadratic_roots(1, -3, 2, Roots).
% Roots = [2.0, 1.0].

% ?- quadratic_roots(1, 2, 1, Roots).
% Roots = [-1.0].

% ?- quadratic_roots(1, 0, 1, Roots).
% Roots = [].
