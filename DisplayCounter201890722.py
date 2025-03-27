/**
 * 4-bit Counter with 7-Segment Display Output
 * Group: [Your Group Number]
 * Uses Week 7's decoder to display 0-F
 */
CHIP DisplayCounter201890722 {
    IN inc, reset;
    OUT a, b, c, d, e, f, g;

    PARTS:
    // 4-bit register to store current count
    Register(in=nextCount, load=inc, out=currentCount, out[0..3]=decoderInput);

    // Increment logic
    Inc16(in=currentCount, out=incremented);
    Mux16(a=currentCount, b=incremented, sel=inc, out=countAfterInc);

    // Reset logic
    Mux16(a=countAfterInc, b=false, sel=reset, out=nextCount);

    // Convert binary to 7-segment output
    DecoderSegment201890722(
        A=decoderInput[0],
        B=decoderInput[1],
        C=decoderInput[2],
        D=decoderInput[3],
        a=a, b=b, c=c, d=d, e=e, f=f, g=g
    );
}