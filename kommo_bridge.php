<?php
// kommo_bridge.php - Versão Thiago Pneus (FORÇADA PARA TESTE)

// 1. Carregar variáveis do .env
function getEnvData($path) {
    if (!file_exists($path)) return [];
    $lines = file($path, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    $data = [];
    foreach ($lines as $line) {
        if (strpos(trim($line), '#') === 0 || !strpos($line, '=')) continue;
        list($name, $value) = explode('=', $line, 2);
        $data[trim($name)] = trim($value);
    }
    return $data;
}

$env = getEnvData(__DIR__ . '/.env');

// 2. Receber dados do Frontend
$json = file_get_contents('php://input');
$dados = json_decode($json, true);

if (!$dados) {
    http_response_code(400);
    echo json_encode(["status" => "error", "message" => "Dados inválidos"]);
    exit;
}

// 3. ROTEAMENTO FORÇADO (TESTE AUTOMAÇÃO ZOOP)
// Se não encontrar no .env, assume os IDs de teste diretamente.
$id_pipeline = 13517452; 
$id_status = 104289080; 

// Se o .env tiver IDs, eles podem sobrescrever, mas vamos dar log para debug se necessário
if (!empty($env['ID_PIPELINE'])) $id_pipeline = (int)$env['ID_PIPELINE'];
if (!empty($env['ID_STATUS'])) $id_status = (int)$env['ID_STATUS'];

// 4. Preparar Payload
$leadCustomFields = [];
$contactCustomFields = [];

// UTMs -> Lead
$utm_mapping = ['utm_source' => 'ID_UTM_SOURCE', 'utm_medium' => 'ID_UTM_MEDIUM', 'utm_campaign' => 'ID_UTM_CAMPAIGN', 'utm_content' => 'ID_UTM_CONTENT', 'utm_term' => 'ID_UTM_TERM', 'fbclid' => 'ID_FBCLID'];
foreach ($utm_mapping as $key => $envKey) {
    if (!empty($dados[$key]) && !empty($env[$envKey])) {
        $leadCustomFields[] = ["field_id" => (int)$env[$envKey], "values" => [["value" => $dados[$key]]]];
    }
}

// Thiago Pneus -> Contact
if (!empty($dados['veiculo']) && !empty($env['ID_FIELD_VEICULO'])) $contactCustomFields[] = ["field_id" => (int)$env['ID_FIELD_VEICULO'], "values" => [["value" => $dados['veiculo']]]];
if (!empty($dados['qtd']) && !empty($env['ID_FIELD_QTD'])) $contactCustomFields[] = ["field_id" => (int)$env['ID_FIELD_QTD'], "values" => [["value" => $dados['qtd']]]];
if (!empty($dados['instalacao']) && !empty($env['ID_FIELD_INSTALACAO'])) $contactCustomFields[] = ["field_id" => (int)$env['ID_FIELD_INSTALACAO'], "values" => [["value" => $dados['instalacao']]]];
if (!empty($dados['quando']) && !empty($env['ID_FIELD_URGENCIA'])) $contactCustomFields[] = ["field_id" => (int)$env['ID_FIELD_URGENCIA'], "values" => [["value" => $dados['quando']]]];

// Multitext
$tel = $dados['tel'] ?? $dados['telefone'] ?? "";
if ($tel) $contactCustomFields[] = ["field_code" => "PHONE", "values" => [["value" => $tel, "enum_code" => "WORK"]]];
$email = $dados['email'] ?? $dados['email_real'] ?? "";
if ($email) $contactCustomFields[] = ["field_code" => "EMAIL", "values" => [["value" => $email, "enum_code" => "WORK"]]];

$payload = [[
    "name" => "Lead Thiago Pneus: " . ($dados['nome'] ?? 'Novo Lead'),
    "status_id" => $id_status,
    "pipeline_id" => $id_pipeline,
    "custom_fields_values" => $leadCustomFields,
    "_embedded" => [
        "contacts" => [[
            "first_name" => $dados['nome'] ?? 'Sem Nome',
            "custom_fields_values" => $contactCustomFields
        ]]
    ]
]];

// 5. Enviar
$subdomain = $env['KOMMO_SUBDOMAIN'] ?? 'thiagopneus';
$token = $env['KOMMO_TOKEN'] ?? '';
$url = "https://{$subdomain}.kommo.com/api/v4/leads/complex";

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
curl_setopt($ch, CURLOPT_HTTPHEADER, ['Authorization: Bearer ' . $token, 'Content-Type: application/json']);
$response = curl_exec($ch);
$statusCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

http_response_code($statusCode);
header('Content-Type: application/json');
echo $response;
?>
