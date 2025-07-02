from mcp.server.fastmcp import FastMCP

mcp= FastMCP("math")

@mcp.tool()
def add(a:int, b:int)->int:
    """_summary_
    add to number
    """
    return a+b

@mcp.tool()
def multiply(a:int,b:int)->int:
    """multiply two numbers"""
    return a*b


## the transport = stdio informs server to use standard
## input / output(stdin,stdout) to tool function call.

if __name__=="__main__":
    mcp.run(transport="stdio")
