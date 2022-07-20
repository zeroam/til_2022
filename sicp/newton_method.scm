(define (sqrt x)
  (sqrt-iter 1.0 x)
)

(define (sqrt-iter guess x)
  (if (good-enough? guess x)
    guess
    (sqrt-iter (improve guess x) x)
  )
)

(define (good-enough? guess x)
  (< (abs (- (square guess) x)) 0.001)
)

(define (improve guess x)
  (average guess (/ x guess))
)

(define (average x y)
  (/ (+ x y) 2)
)


; 3.00009155413138
(sqrt 9)
; 11.704699917758145
(sqrt (+ 100 37))
; 1000.000369924366
(square (sqrt 1000))