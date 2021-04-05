section	.text
	global main
	extern printf
main:
    mov rbx, 0 ; sum
    mov rsi, nums; initial offset (first el)
    mov rcx, nums_len ; loop counter
    inc rcx ; for the initial check jump
    jmp check
    summing:
	add rbx, rax
	dec rcx ;  
        cmp rcx, 0
        je exit
    test_loop:
        mov rax, [rsi]
        add rsi, 8 ; moving on to the next num  
        mov rdx, rax
        and rdx, 68 ; mask
        xor rdx, 68
        je summing
    check:
	dec rcx
	cmp rcx, 0
	jne test_loop
    exit:
	mov [sum], rbx
        ; printing the answer
        mov rdi, msg ; format 
        mov rsi, [sum] ; 1st param
        mov rax,0
        call printf        
	; exit
	mov rax, 1
	mov rbx, 0 ; return code
	int 0x80
section .data 
	msg db "Sum: %d", 0xA, 0 
	msg_len equ $-msg
	nums dq 84, 190, 86, 244, 216, 220, 255, 227, 231, 235 
	nums_len equ 10
	sum dq 0 

