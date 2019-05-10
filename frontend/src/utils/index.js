export const makeSimpleRequest = async requestString => {
  const apiRoot = process.env.API_ROOT
  const apiEndpointUrl = new URL(`${apiRoot}/simple`)
  const params = {
    'request': requestString.replace(/\s+/g, ' ')
  }
  apiEndpointUrl.search = new URLSearchParams(params)
  const response = await fetch(apiEndpointUrl)
  return readBlob(await response.blob())
}

const readBlob = async blob => {
  return new Promise((resolve, reject) => {
    const reader = new FileReader()
    reader.onload = () => {
      resolve(reader.result)
    }
    reader.onerror = reject
    reader.readAsDataURL(blob)
  })
}
