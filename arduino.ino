// Controle de 2 motores por Bluetooth (HC-05/HC-06)
// Comandos:
// '2' = frente
// '5' = tras
// '3' = direita
// '1' = esquerda
// '0' = parar

const int M1_IN1 = 5;
const int M1_IN2 = 10;
const int M2_IN1 = 6;
const int M2_IN2 = 11;

void pararMotores() {
	digitalWrite(M1_IN1, LOW);
	digitalWrite(M1_IN2, LOW);
	digitalWrite(M2_IN1, LOW);
	digitalWrite(M2_IN2, LOW);
}

void frente() {
	// Ambos motores para frente
	digitalWrite(M1_IN1, HIGH);
	digitalWrite(M1_IN2, LOW);
	digitalWrite(M2_IN1, HIGH);
	digitalWrite(M2_IN2, LOW);
}

void tras() {
	// Ambos motores para tras
	digitalWrite(M1_IN1, LOW);
	digitalWrite(M1_IN2, HIGH);
	digitalWrite(M2_IN1, LOW);
	digitalWrite(M2_IN2, HIGH);
}

void direita() {
	// Gira para direita: motor esquerdo frente, direito tras
	digitalWrite(M1_IN1, HIGH);
	digitalWrite(M1_IN2, LOW);
	digitalWrite(M2_IN1, LOW);
	digitalWrite(M2_IN2, HIGH);
}

void esquerda() {
	// Gira para esquerda: motor esquerdo tras, direito frente
	digitalWrite(M1_IN1, LOW);
	digitalWrite(M1_IN2, HIGH);
	digitalWrite(M2_IN1, HIGH);
	digitalWrite(M2_IN2, LOW);
}

void testeMovimentos() {
	frente();
	delay(1000);
	pararMotores();
	delay(400);

	tras();
	delay(1000);
	pararMotores();
	delay(400);

	direita();
	delay(800);
	pararMotores();
	delay(400);

	esquerda();
	delay(800);
	pararMotores();
	delay(400);
}

void setup() {
	pinMode(M1_IN1, OUTPUT);
	pinMode(M1_IN2, OUTPUT);
	pinMode(M2_IN1, OUTPUT);
	pinMode(M2_IN2, OUTPUT);

	pararMotores();

	// Bluetooth no Serial (HC-05/HC-06 em 9600)
	Serial.begin(9600);

	// Teste automatico inicial: frente, tras, direita e esquerda
	testeMovimentos();
}

void loop() {
	if (Serial.available() > 0) {
		char comando = Serial.read();

		switch (comando) {
			case '2':
				frente();
				break;

			case '5':
				tras();
				break;

			case '3':
				direita();
				break;

			case '1':
				esquerda();
				break;

			case '0':
				pararMotores();
				break;

			default:
				// Ignora comandos desconhecidos
				break;
		}
	}
}
