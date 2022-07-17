(define (a-plus-abs-b a b)
  ((if (> b 0) + -) a b)
)

; 7
(a-plus-abs-b 3 4)
; 7
(a-plus-abs-b 3 -4)