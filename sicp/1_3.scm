(define (square x) (* x x))

(define (square_sum x y) (+ (square x) (square y)))

(define (two_square_sum x y z)
    (cond
        ((and (>= (+ x y) (+ x z)) (>= (+ x y) (+ y z))) (square_sum x y))
        ((and (>= (+ x z) (+ x y)) (>= (+ x z) (+ y z))) (square_sum x z))
        (else (square_sum y z))
    )
)

; 13
(two_square_sum 1 2 3)
; 2
(two_square_sum 1 1 1)
; 8
(two_square_sum 1 2 2)
; 5
(two_square_sum 1 1 2)
; 34
(two_square_sum 1 3 5)