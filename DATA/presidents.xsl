<?xml version="1.0" encoding="UTF-8"?>
<!-- output to simple HTML table  -->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:template match="/">
    <html>
    <body>
    <table border="2">
      <tr><th>Term</th><th>President</th><th>Birth State</th><th>Term</th></tr>
      <xsl:for-each select="presidents/president">
        <tr>
          <td><xsl:value-of select="index"/></td>
          <td><xsl:value-of select="name/first"/><xsl:text> </xsl:text><xsl:value-of select="name/last"/></td>
          <td><xsl:value-of select="birthstate"/></td>
          <td>
            <xsl:value-of select="termstart/month"/><xsl:text> </xsl:text><xsl:value-of select="number(termstart/day)"/>, <xsl:value-of select="termstart/year"/>
            <xsl:text>-</xsl:text>
            <xsl:value-of select="termend/month"/><xsl:text> </xsl:text><xsl:value-of select="number(termend/day)"/>, <xsl:value-of select="termend/year"/>
          </td>    
        </tr>
      </xsl:for-each>
   </table>
    </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
