from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister,BasicAer, execute

def quantum_examples(operator,count,l):
    backend = BasicAer.get_backend('qasm_simulator')
    if l == 1:
        q = QuantumRegister(1)
        c = ClassicalRegister(1)  
        sp_state = QuantumCircuit(q, c)
    elif l == 2:
        q = QuantumRegister(2)
        c = ClassicalRegister(2) 
        sp_state = QuantumCircuit(q, c)
        sp_state.cs(q[0],q[1])
    if operator == 'x':
        print(f'Выполнение вентиля Паули X на {count} повторений')
        sp_state.x(q)
        sp_state.measure(q,c)       
        result = execute(sp_state, backend, shots = count).result()
        print(result.get_counts(sp_state))  
    elif operator == 'h':
        print(f'Выполнение вентиля Адамара на {count} повторений')
        sp_state.h(q)
        sp_state.measure(q,c)
        result = execute(sp_state, backend, shots = count).result()
        print(result.get_counts(sp_state))  
    elif operator == 'z':
        print(f'Выполнение вентиля Адамара на {count} повторений')
        sp_state.z(q)
        sp_state.measure(q,c)
        result = execute(sp_state, backend, shots = count).result()
        print(result.get_counts(sp_state))  
    elif operator == 'hh':
        print(f'Двойное выполнение вентиля Адамара на {count} повторений')
        sp_state.h(q)  
        sp_state.h(q)    
        sp_state.measure(q,c)
        result = execute(sp_state, backend, shots = count).result()
        print(result.get_counts(sp_state))   
    else:
        return   

for i in ('x','h','hh'):
    quantum_examples(i,2048,1)

for i in ('x','h','hh'):
    quantum_examples(i,2048,2)












