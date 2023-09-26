# Monitoramento_de_produto_Mercado_Livre
#### Software com a funcionalidade de coletar dados de todos os anúncios disponíveis sobre determinado produto e armazená-los em um arquivo .csv.

## Procedimentos
#### Inicialmente realizei as pré-definições do ambiente e da biblioteca que seriam utilizados. Para esse projeto de web scraping optei por utilizar a biblioteca Selenium.

#### Após as pré-definições feitas, iniciei meu Driver (o navegador a ser utilizado), já indicando-o o site que seriam obtidos os dados, que nesse caso o endereço web de destino já constava a pesquisa do produto.

#### Ao entrar no site definido aguardei 5 minutos para começarmos o scraping dos dados, evitando assim que o site derrubasse a automação alegando ser algum bot, utilizei esse tempo padrão de 5 minutos para iniciar o scraping sempre que o bot trocava de página.

#### Iniciando o scraping, o software realiza um scroll (rolamento) até o final da página para que ela fosse totalmente carregada, evitando que algum anúncio fosse deixado de fora do scraping. Com isso feito, obtive todos os elementos comuns que se caracterizavam como anúncios, buscando primeiramente os títulos dos anúncios, segundamente os preços e terceiramente os links de acesso de cada anúncio.

#### Com todos esses dados em mãos, o procedimento final seria armazená-los em um arquivo CSV, arquivo esse que possui uma estrutura parecida com a do excel, porém separando cada coluna por um determinado tipo de separador, nesse projeto optei por utilizar o separador ; para não entrar em conflito com os dados de alguns títulos ou outra propriedade obtida. 
