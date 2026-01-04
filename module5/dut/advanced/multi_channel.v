/**
 * Module 5: Multi-Channel Interface
 * 
 * A multi-channel interface for advanced UVM testing.
 * 
 * Ports:
 *   clk:        Clock signal
 *   rst_n:      Active-low reset
 *   master_valid: Master channel valid
 *   master_ready: Master channel ready
 *   master_data:  Master channel data
 *   slave_valid:  Slave channel valid
 *   slave_ready:  Slave channel ready
 *   slave_data:   Slave channel data
 */

module multi_channel (
    input  wire       clk,
    input  wire       rst_n,
    input  wire       master_valid,
    output reg        master_ready,
    input  wire [7:0] master_data,
    input  wire       slave_valid,
    output reg        slave_ready,
    input  wire [7:0] slave_data
);

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            master_ready <= 1'b0;
            slave_ready <= 1'b0;
        end else begin
            if (master_valid) begin
                master_ready <= 1'b1;
            end else begin
                master_ready <= 1'b0;
            end
            
            if (slave_valid) begin
                slave_ready <= 1'b1;
            end else begin
                slave_ready <= 1'b0;
            end
        end
    end

endmodule

