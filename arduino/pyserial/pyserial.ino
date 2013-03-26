int incomingByte = 0;

int redPin = 3;
int greenPin = 4;
int bluePin = 5;
int buzzerPin = 6;

void setup() {
    Serial.begin(9600);

    pinMode( redPin, OUTPUT );
    pinMode( bluePin, OUTPUT );
    pinMode( greenPin, OUTPUT );
}

// freq in hz, t in ms
void freqout(int freq, int t) {
    int hperiod;                               //calculate 1/2 period in us
    long cycles, i;
    pinMode(buzzerPin, OUTPUT);                   // turn on output pin

    hperiod = (500000 / freq) - 7;             // subtract 7 us to make up for digitalWrite overhead

    cycles = ((long)freq * (long)t) / 1000;    // calculate cycles

    for (i=0; i<= cycles; i++){              // play note for t ms 
        digitalWrite(buzzerPin, HIGH); 
        delayMicroseconds(hperiod);
        digitalWrite(buzzerPin, LOW); 
        delayMicroseconds(hperiod - 1);     // - 1 to make up for digitaWrite overhead
    }
    
    pinMode(buzzerPin, INPUT);                // shut off pin to avoid noise from other operations
}

void loop() {
        if (Serial.available() > 0) {
                incomingByte = Serial.read();

                if( incomingByte == 119 ) {
                    digitalWrite( bluePin, HIGH );
                    freqout( 31608, 250 );
                    delay( 500 );
                    digitalWrite( bluePin, LOW );
                }
        }
}